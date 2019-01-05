[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/AndersonUyekita/ND110_data_science_foundations_01/master?filepath=%2F02-Chapter_02%2F00-Project_01%2Fudacity_nd110_project_01.ipynb)

# Project 01 - Explore Chicago Bikeshare Data

#### Tags
* Title: Project 01 - Explore Chicago Bikeshare Data
* Author: AH Uyekita
* Date: 07/12/2018
* Cod: nd110

## Objectives

Complete the `chicago_bikeshare.py` file coding the 11 tasks.

For further information read the [notes_project_01.md](https://github.com/AndersonUyekita/udacity_data_science_foundation_01/blob/master/02-Part_02/01-Project/udacity_nd110_project_01.md)

#### Memo
```
jupyter notebook --notebook-dir='D:/'
```

****************************************************
## 1. Project Overview (Instructions)

### Overview

In this project, you will make use of Python to explore data related to bike share systems for Chicago. You will write code to import the data and answer interesting questions about it by computing descriptive statistics. You will also create some important functions and plot charts.

### What Software Do I Need?

To complete this project, the following software requirements apply:

* Python 3. The following packages in the Python Standard Library will likely be useful: csv and matplotlib.
* A text editor, like Sublime or Atom.
* A terminal application (Terminal on Mac and Linux or Cygwin on Windows).

## 2. Project Details

### Bike Share Data

Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, you will use data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. You will use the data from one of the largest cities of United States: Chicago.

### The Datasets

Data for the first six months of 2017 are provided. The data file contain six (6) columns:

* Start Time (e.g. 2017-01-01 00:07:57)
* End Time (e.g. 2017-01-01 00:20:53)
* Trip Duration (in seconds, e.g., 776)
* Start Station (e.g. Broadway & Barry Ave)
* End Station (e.g. Sedgwick St & North Ave)
* User Type (Subscriber or Customer)
* Gender (Male or Female)
* Birth Year (e.g., 1980)


The original files, which can be accessed here (Chicago, New York City, Washington), had more columns and they differed in format in many cases. Some data wrangling has been performed to condense these files to the above core six columns to make your analysis and the evaluation of your Python skills more straightforward. In the Data Wrangling course that follows this course in the Data Analyst Nanodegree program, students learn how to wrangle the dirtiest, messiest datasets so don't fret if you worried about missing out.

### The Questions

You will write code to complete the following tasks:

* Task 1: Print the first 20 samples(rows) from the database
* Task 2: Print the gender(column) of the first 20 samples
* Task 3: Create a function to get the columns as a list
* Task 4: Count how many of each gender do we have
* Task 5: Create a function to count the genders
* Task 6: Show the most popular gender
* Task 7: Plot a a chart using the previous data
* Task 8: Answer why summing the number of Males and Females doesn't match the number of samples
* Task 9: Find the minimum, maximum, mean and median duration of the trips
* Task 10: Get all the start stations of the dataset
* Task 11: Create a function count the occurrence of any given column (optional)

### The Files

To answer these questions using Python, you will need to write a Python script. To help guide your work in this project, a template with helper code and comments is provided as a downloadable .py file. You will also need the dataset file. All of the following files are available for download.

chicago_bikeshare_pt.zip

* bikeshare.py
* chicago.csv
*
Once you have downloaded this zip file, move to the next page for more details on the code you will be writing.

## 3. Code Walkthrough

### _TODOs_
All of the code you must fill out in chicago_bikeshare_en.py is marked in comments that start with "TODO". Take a detailed read through that file to get a gauge for how the script flows and the additions you will have to make to complete this project.

### _ASSERTs_
We are using the assert to make sure your code is returning an expected value or an output in the right format. DO NOT CHANGE IT. If you can't pass through an assert, ask for help.

### _The `csv` Module_
The csv module is core to completing this project. One thing to be careful about—these bikeshare CSV files are quite large so iterating through them will be costly in terms of compute time.

* Be sure to bite off bits of code that you can chew and regularly test your code as you develop it. Print statements are your friend.
* Do not try to open the CSV with a text editor. It may crash your computer.
* Load each CSV file into a data structure once at the beginning of the script rather than at the beginning of every function. Hint: You may use the code as it was proposet (with a list of lists), but converting the DictReader iterator into a list of dictionaries (as described in this Stack Overflow post) could be handy! You only need to do the properly changes.

If you are familiar with NumPy and/or pandas, you may realize that using the csv module is much less efficient than these libraries tailored for data analysis. The csv module is used in this project so foundational programming skills can be tested, as well as to gain an appreciation for the speed at which NumPy and pandas (which are taught later) can do their calculations on large files. Do not use those libraries.

## 4. Project Submission `Due Jan 04/2019`

In this project, you will write Python code deal with the Chicago bike share data and answer interesting questions about it by computing descriptive statistics. You will also write practical functions to show your skills in Python. The initial code and dataset is available here.

### Before You Submit

#### Check the Rubric

Your project will be evaluated by a Udacity reviewer according to this Project Rubric. Be sure to review it thoroughly before you submit. Your project "meets specifications" only if it meets specifications in all the criteria. If you see room for improvement in any category in which you do not meet specifications, be sure to take some time to revise your work until you feel it is up to expectations. In particular, there is one section of the rubric that cares about the quality of your code. It is important that you not only obtain the correct answers with your code, but that you have followed good coding practices to obtain your solutions.

#### Gather Submission Materials

All you need to submit for this project is:

* chicago_bikeshare_en.py: Your code

There is no need for you to include any data files with your submission.

### Submitting the Project

When you're ready, click on the "Submit Project" button to go to the project submission page. You can submit your files as a .zip archive or you can link to a GitHub repository containing your project files. If you go with GitHub, note that your submission will be a snapshot of the linked repository at the time of submission. It is recommended that you keep each of your projects in a separate repository to avoid any potential confusion: if a reviewer gets multiple folders representing multiple projects, there might be confusion regarding what project is to be evaluated.

It can take us up to a week to grade the project, but in most cases it is much faster. You will get an email once your submission has been reviewed. If you are having any problems submitting your project or wish to check on the status of your submission, please email us at suporte@udacity.com. In the meantime, you should feel free to proceed with your learning journey by continuing on to the next module in the program.
