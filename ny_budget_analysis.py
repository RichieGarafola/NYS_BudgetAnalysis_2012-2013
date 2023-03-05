import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
url = 'https://data.ny.gov/resource/62eq-hqts.csv'
df = pd.read_csv(url)

# Rename columns and drop unnecessary columns
df = df.rename(columns={
    'bfy': 'Budget Year',
    'fund_cd': 'Fund Code',
    'dept_cd': 'Department Code',
    'dept_nm': 'Department Name',
    'unit_cd': 'Unit Code',
    'unit_nm': 'Unit Name',
    'obj_cd': 'Object Code',
    'obj_nm': 'Object Name',
    'actv_cd': 'Activity Code',
    'actv_nm': 'Activity Name',
    'appr_cd': 'Appropriation Code',
    '_2010_actuals': 'Actuals 2010',
    '_2011_actuals': 'Actuals 2011',
    '_2012_modified': 'Modified 2012',
    '_2012_adopted': 'Adopted 2012',
    '_2012_estimated': 'Estimated 2012',
    '_2013_requested': 'Requested 2013',
    '_2013_recommended': 'Recommended 2013',
    '_2013_adopted': 'Adopted 2013'
})

df = df.drop(['Fund Code', 'Activity Code', 'Activity Name', 'Unit Code', 'Unit Name', 'Modified 2012', 'Adopted 2012', 'Requested 2013', 'Recommended 2013', 'Adopted 2013'], axis=1)

# Remove leading and trailing white space from string columns
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Set page title and favicon
st.set_page_config(page_title='NY State Budget Analysis', page_icon=':chart_with_upwards_trend:')

# Set sidebar title and icon
st.sidebar.title('Menu')
st.sidebar.image('https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Flag_of_New_York.svg/510px-Flag_of_New_York.svg.png', use_column_width=True)

# Add dropdown menu for selecting KPI
kpi_options = {
    'Top 10 Departments or Units by Total Budgetary Expenses': 1,
    'Top 10 Types of Expenses by Percentage of Total Budget': 2,
    'Total Budget by Department': 3,
    'Mean Percentage Difference Between Estimated and Actual Budgets by Department': 4,
    'Proportion of Budget by Object Code': 5
}
kpi_selection = st.sidebar.selectbox('Select a KPI', list(kpi_options.keys()))

# Define function to format large numbers with commas
def format_number(num):
    if isinstance(num, float):
        num = round(num, 2)
    return f'{num:,}'

# Define function to plot horizontal bar chart
def plot_bar_chart(data, title, x_label, y_label):
    fig, ax = plt.subplots()
    ax.barh(data.index, data)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    st.pyplot(fig)

# Define function to plot vertical bar chart
def plot_vertical_bar_chart(data, title, x_label, y_label):
    fig, ax = plt.subplots()
    ax.bar(data.index, data)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    st.pyplot(fig)

def plot_pie_chart(df, col):
    '''
    Plots a pie chart showing the distribution of values in a specified column of a Pandas DataFrame.
    
    Parameters:
    df (Pandas DataFrame): the DataFrame containing the data to be plotted
    col (str): the name of the column to be plotted
    
    Returns:
    None
    '''
    # Group the data by the specified column and calculate the total count for each group
    grouped_data = df.groupby(col).size().reset_index(name='count')
    
    # Sort the data by count in descending order and keep only the top 10 groups
    sorted_data = grouped_data.sort_values('count', ascending=False).head(10)
    
    # Create a pie chart using matplotlib
    fig, ax = plt.subplots()
    ax.pie(sorted_data['count'], labels=sorted_data[col], autopct='%1.1f%%', startangle=90, textprops={'fontsize': 10})
    ax.axis('equal')
    
    # Add a title to the chart
    ax.set_title(f'Distribution of {col}', fontsize=14)
    
    # Display the chart
    st.pyplot(fig)

if kpi_selection == 'Top 10 Departments or Units by Total Budgetary Expenses':
    # Group the data by department and sum the total budgetary expenses for each department
    department_data = df.groupby('Department Name')['Actuals 2010'].sum().sort_values(ascending=False).head(10)
    
    # Plot a horizontal bar chart of the top 10 departments by total budgetary expenses
    plot_bar_chart(department_data, 'Top 10 Departments by Total Budgetary Expenses', 'Total Budgetary Expenses ($)', 'Department Name')

elif kpi_selection == 'Top 10 Types of Expenses by Percentage of Total Budget':
    # Group the data by object and sum the total budgetary expenses for each object
    object_data = df.groupby('Object Name')['Actuals 2010'].sum().sort_values(ascending=False)
    
    # Calculate the percentage of total budget each object represents
    object_data_percentage = object_data / object_data.sum() * 100
    
    # Take the top 10 objects by percentage of total budget
    object_data_top_10 = object_data_percentage.head(10)
    
    # Plot a horizontal bar chart of the top 10 objects by percentage of total budget
    plot_bar_chart(object_data_top_10, 'Top 10 Types of Expenses by Percentage of Total Budget', 'Percentage of Total Budget', 'Object Name')

elif kpi_selection == 'Total Budget by Department':
    # Group the data by department and sum the total budgetary expenses for each department
    department_data = df.groupby('Department Name')['Actuals 2010'].sum().sort_values(ascending=False)
    
    # Plot a vertical bar chart of the total budget by department
    plot_vertical_bar_chart(department_data, 'Total Budget by Department', 'Department Name', 'Total Budgetary Expenses ($)')

elif kpi_selection == 'Mean Percentage Difference Between Estimated and Actual Budgets by Department':
    # Calculate the mean percentage difference between estimated and actual budgets for each department
    df['Percentage Difference'] = (df['Estimated 2012'] - df['Actuals 2010']) / df['Actuals 2010'] * 100
    department_data = df.groupby('Department Name')['Percentage Difference'].mean().sort_values(ascending=False)
    
    # Plot a vertical bar chart of the mean percentage difference by department
    plot_vertical_bar_chart(department_data, 'Mean Percentage Difference Between Estimated and Actual Budgets by Department', 'Department Name', 'Mean Percentage Difference (%)')

elif kpi_selection == 'Proportion of Budget by Object Code':
    # Group the data by object code and sum the total budgetary expenses for each object code
    object_data = df.groupby('Object Code')['Actuals 2010'].sum().sort_values(ascending=False)
    
    # Plot a pie chart of the proportion of budget by object code
    plot_pie_chart(df, 'Object Code')
