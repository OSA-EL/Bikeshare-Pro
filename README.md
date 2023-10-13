# Bikeshare Analysis-Project
An analysis for bikeshare application Data for some cities in USA

## Step 1:

### Understanding the Data
Introduction

Though there are a number of ways you can go about tackling this project, we recommend using NumPy and pandas. Using these libraries is the industry standard for working with data in Python. In the quizzes in this and the following sections, you will get some practice using NumPy and pandas to complete different parts of the project. Then for the project, you will need to piece your code together with some additional code to complete a final project! These sections will likely be helpful if you use NumPy and pandas to complete the project.
Understanding the Data

Let's use pandas to better understand the bike share data! Use this code editor to explore chicago.csv and answer the questions below. The file included here is a mini version of one of the actual data files you will work with for the project. It only includes 400 rows, but the structure and columns are the same.

    What columns are in this dataset?
    Are there any missing values?
    What are the different types of values in each column?

### Some useful pandas methods:

    df.head()
    df.columns
    df.describe()
    df.info()
    df['column_name'].value_counts()
    df['column_name'].unique()


## Step 2:

These three practice problems in the following few sections will help you prepare for the project. These problems use the same mini version of the actual chicago.csv dataset that you will use for the project.
Practice Problem #1: Compute the Most Popular Start Hour

Use pandas to load chicago.csv into a dataframe, and find the most frequent hour when people start traveling. There isn't an hour column in this dataset, but you can create one by extracting the hour from the "Start Time" column. To do this, you can convert "Start Time" to the datetime datatype using the pandas to_datetime() method and extracting properties such as the hour with these properties.

Hint: Another way to describe the most common value in a column is the mode.

Step 3:

### Practice Problem #1

These three practice problems in the following few sections will help you prepare for the project. These problems use the same mini version of the actual chicago.csv dataset that you will use for the project.
Practice Problem #1: Compute the Most Popular Start Hour

Use pandas to load chicago.csv into a dataframe, and find the most frequent hour when people start traveling. There isn't an hour column in this dataset, but you can create one by extracting the hour from the "Start Time" column. To do this, you can convert "Start Time" to the datetime datatype using the pandas to_datetime() method and extracting properties such as the hour with these properties.

Hint: Another way to describe the most common value in a column is the mode.

### Practice Problem #2

Display a Breakdown of User Types

There are different types of users specified in the "User Type" column. Find how many there are of each type and store the counts in a pandas Series in the user_types variable.
Hint: What pandas function returns a Series with the counts of each unique value in a column?

### Practice Problem #3

Load and Filter the Dataset

This is a bit of a bigger task, which involves choosing a dataset to load and filtering it based on a specified month and day. In the quiz below, you'll implement the load_data() function, which you can use directly in your project. There are four steps:

- Load the dataset for the specified city. Index the global CITY_DATA dictionary object to get the corresponding filename for the given city name.
- Create month and day_of_week columns. Convert the "Start Time" column to datetime and extract the month number and weekday name into separate columns using the datetime module.
- Filter by month. Since the month parameter is given as the name of the month, you'll need to first convert this to the corresponding month number. Then, select rows of the dataframe that have the specified month and reassign this as the new dataframe.
- Filter by day of week. Select rows of the dataframe that have the specified day of week and reassign this as the new dataframe. (Note: Capitalize the day parameter with the title() method to match the title case used in the day_of_week column!)
    
