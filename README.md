# NYS Budget Analysis 2012 - 2013

Deployable Streamlit App: 
https://nybudgetkpi20122013.streamlit.app/

---

Welcome to the New York State Budget Analysis project! This project is aimed at providing insights into the budgetary expenses of each department and unit of government in New York State from 2010 to 2013. The data used in this project is obtained from the New York State Open Data Portal, and we have provided a detailed description of the columns in the dataset to help you understand the data better.

This project is useful for anyone who is interested in understanding how the New York State government allocates its funds. It provides insights into which departments or units have the highest budgetary expenses, the most common types of expenses across all departments or units, and how the budget for each department or unit has changed over the years.

To run the code, you need to have a Python environment set up, and the required packages installed. We have provided detailed instructions on how to install the required packages using pip. The code includes various analyses, each with code to display the results graphically.

We hope that this project will help you gain insights into the New York State budget and be a useful resource for anyone interested in understanding how the government allocates its funds. Feel free to contribute to the project or suggest improvements!

---

## The columns in the dataset are:

budget_year: the fiscal year of the budget

department_code: the code for the department the budget is for

department_name: the name of the department the budget is for

unit_code: the code for the unit the budget is for

unit_name: the name of the unit the budget is for

object_code: the code for the object the budget is for (e.g. salaries, equipment, supplies)

object_name: the name of the object the budget is for

appropriation_code: the code for the appropriation (the money that has been allocated) for the object

actuals_2010: the actual spending for the object in fiscal year 2010

actuals_2011: the actual spending for the object in fiscal year 2011

modified_2012: the amount of the appropriation that was modified for the object in fiscal year 2012

adopted_2012: the amount of the appropriation that was adopted for the object in fiscal year 2012

estimated_2012: the estimated spending for the object in fiscal year 2012

requested_2013: the amount of the appropriation that was requested for the object in fiscal year 2013

recommended_2013: the amount of the appropriation that was recommended for the object in fiscal year 2013

adopted_2013: the amount of the appropriation that was adopted for the object in fiscal year 2013

---

## Requirements
This project requires the following packages to be installed:

    - pandas
    - numpy
    - matplotlib
    - requests
    
You can install these packages using pip:


    pip install pandas numpy matplotlib requests

---

## Usage

To run the code, open the Python file ny_budget_analysis.py in a Python environment, such as Jupyter Notebook, and run each cell in order.

---

## The notebook code includes the following analyses:

- Which departments or units have the highest budgetary expenses?

- Which types of expenses are most common across all departments or units?

- How has the budget for each department or unit changed over the years?

- Finding the total budget for each department

- Comparing estimated budgets to actual budgets

- Proportion of Budget by Object Code

- Each analysis includes code to display the results graphically.

## The Streamlit KPI includes the following insights

- "Top 10 Departments or Units by Total Budgetary Expenses": This KPI can be used to identify the departments or units that are receiving the highest amount of budgetary expenses. This information can be used to focus on cost-cutting measures in the departments or units that have the highest budgetary expenses.

- "Top 10 Types of Expenses by Percentage of Total Budget": This KPI can help to identify the types of expenses that consume the highest percentage of the budget. This information can be used to identify areas where budget cuts can be made or where there is a need to increase the budget allocation.

- "Total Budget by Department": This KPI provides an overview of the total budget allocated to each department. It can be used to identify the departments that require the most resources and those that have been allocated a lower budget.

- "Mean Percentage Difference Between Estimated and Actual Budgets by Department": This KPI can help to identify the departments that are over or underestimating their budget requirements. This information can be used to identify areas where budget planning needs to be improved or where budget allocation needs to be adjusted.

- "Proportion of Budget by Object Code": This KPI provides an overview of the proportion of the budget allocated to different types of expenses. It can be used to identify the areas where there is a need to increase or decrease budget allocation.
