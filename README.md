##Gender Bias 
###and its cumulative effect on careers and promotions
---

###View Project
####[www.doesgenderbiasmatter.com](www.doesgenderbiasmatter.com)

---

###Getting Started

1. Fork the repository

2. Install virtualenv `$ pip install virtualenv`

3. Cd into project folder `cd doesgenderbiasmatter`

4. Make virtualenv  `$ mkvirtualenv venv`

5. Activate virtualenv `$ source venv/bin/activate`

6. Install requirements file into your virtualenv `$ pip install requirements.txt`

7. Run server `$ python control.py`

8. Deactivate virtualenv `$ deactivate`


---
###Background
The topic of gender bias, particularly in tech companies, is a current one. It's a broad discussion touching on hiring and promotion practices, as well as inclusion in the workplace. 

This project is inspired by this [research paper](http://www.ruf.rice.edu/~lane/papers/male_female.pdf) and illustrates the impact of bias on a simplified dataset.

The simulator starts with an equal number of women and men at each employee level. Level one is entry-level and level eight is executive. The simulator demonstrates 12 promotional cycles, which represents 2 per year for 6 years.

Before each promotional period 15% of employees at all levels are randomly removed, representing a 15% attrition rate. Retained employees are randomly assigned promotion scores from 1-100, or 1-100 + bias amount for the favored gender.

Note: The simulator uses random selection for attrition and promotional scores. So the results will have a small variance.

---
###Authors
This project was built by [Penelope Hill](https://github.com/penelopy) during her the final 2 weeks of her Technical Fellowship at Square. Contributions have been made by [Alyssa Pohahau](https://github.com/alyssa), [Wendy Dherin](https://github.com/doubledherin), and [Dina Westland](https://github.com/dina). The idea for this project came from [Eric Burke](https://github.com/eburke). 

---
###License
See [License](LICENSE.txt) file for license rights and limitations (Apache).








