from flask import Flask, render_template, request
import json

from simulation import Simulation

app = Flask(__name__)
app.debug = True

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/bias', methods=['POST'])
def fetch_bias_amount():
    """Receives button click data (from gender or 'bias percent' buttons) and uses json 
    to send results data to jQuery to populate the graph"""

    bias = request.form.getlist('bias')[0]
    gender = request.form.getlist('gender')[0]

    control = Control(gender, bias)
    control.run_simulations()
    results = control.fetch_results()
    results=json.dumps(results)

    return results

class Control:
    """Runs bias simulations based on "Male-Female Differences: A Computer
    Simulation" from the Feb, 1996 issue of American Psychologist.
    http://www.ruf.rice.edu/~lane/papers/male_female.pdf"""

    def __init__(self, bias_favors_this_gender, promotion_bias):
        self.bias_favors_this_gender = bias_favors_this_gender
        self.promotion_bias = int(promotion_bias)
        self.num_simulations = 30
        self.attrition = 15
        self.iterations_per_simulation = 20
        self.num_positions_at_level = [500, 350, 200, 150, 100, 75, 40, 10]
        self.num_employee_levels = len(self.num_positions_at_level)

    def run_simulations(self):
        """Run NUM_SIMULATIONS simulations"""
        self.results = []
        append = self.results.append
        for _ in xrange(self.num_simulations):
            simulation = Simulation(self.num_simulations, self.attrition, self.iterations_per_simulation, 
                self.promotion_bias, self.num_positions_at_level, self.bias_favors_this_gender)
            simulation.run()
            append(simulation.get_result())

    def fetch_results(self):
        """Creates two lists. Each contains the percent of that gender at each employee level """
        total_men_at_levels = []
        total_women_at_levels = []
        # Setting append constructs here, saves compute time in loop
        men_append = total_men_at_levels.append 
        women_append = total_women_at_levels.append

        for level in range(0, self.num_employee_levels):
            total_num_men = 0.00
            total_num_women = 0.00
            for result in self.results:
                total_num_men += result.men[level]
                total_num_women += result.women[level]

            total_employees = total_num_men + total_num_women
            men_percentage = 100 * total_num_men / total_employees
            women_percentage = 100 * total_num_women / total_employees

            men_append(men_percentage)
            women_append(women_percentage)
        return [total_men_at_levels, total_women_at_levels, self.promotion_bias, self.bias_favors_this_gender]

    def print_header(self):
        """Print header with variable info"""
        print 
        print("Running {} simulations.".format(self.num_simulations))
        print("{0:2}% bias for men".format(self.promotion_bias))
        print("{0:2} promotion cycles".format(self.iterations_per_simulation))
        print("{0:2}% attrition rate".format(self.attrition))
        print "Attrition is random"

    def print_summary(self):
        """Print summary is a replica of 'fetch_results' method used strictly for viewing data"""
        print("Level\tMen\tWomen")
        print("%\t\t%")
        print("-----\t-----------------")

        total_men_at_levels = []
        total_women_at_levels = []
        # Setting append constructs here, saves compute time in loop
        men_append = total_men_at_levels.append 
        women_append = total_women_at_levels.append

        for level in range(0, self.num_employee_levels):
            total_num_men = 0.00
            total_num_women = 0.00
            for result in self.results:
                total_num_men += result.men[level]
                total_num_women += result.women[level]

            total_employees = total_num_men + total_num_women
            men_percentage = 100 * total_num_men / total_employees
            women_percentage = 100 * total_num_women / total_employees

            men_append(men_percentage)
            women_append(women_percentage)

            summary = "%d\t%.2f\t%.2f" %(level + 1, men_percentage, women_percentage)
            print summary
        print 



if __name__ == "__main__": 
    # Printing & Testing
    # control = Control('men', 5)
    # control.run_simulations()
    # control.print_header()
    # summary = control.print_summary()

    # Running app 
    app.run()
    control = Control('men', 1)
    control.run_simulations()
    results = control.fetch_results()
