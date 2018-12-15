# Project 01 - Explore Chicago Bikeshare Data

#### Tags
* Title: Project 01 - Explore Chicago Bikeshare Data
* Author: AH Uyekita
* Date: 07/12/2018
* Cod: nd110
* Tags: Udacity, Data Science, Python

## Setup

I have performed this project using:

* Atom (1.33.0);
* Spider (3.3.1).

## TODO

* Comment each Task.

### Task 1

```{py}
# TASK 1
# TO DO: Print the first 20 rows using a loop to identify the data.
for i in range(0,20):   # The first 20 rows - The first row in the header and the other 19 rows were observations
    print(data_list[i]) # Printing
```


### Task 2

```{py}
# TASK 2
# TO DO: Print the `gender` of the first 20 rows

for i in range(0,20):   # The first 20 rows
    print(data_list[i][6])
```

### Task 3

```{py}
# TASK 3
# TO DO: Create a function to add the columns(features) of a list in another list in the same order
def column_to_list(data, index):
    """
    -----------------------------------------------------------------------------------------------------
    |DESCRIPTION:                                                                                       |
    |                                                                                                   |
    |     This function selects a specific column (defined as index) of a data frame (here called       |
    |     as data, but probabily will be data_list).                                                    |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |INPUT:                                                                                             |
    |                                                                                                   |
    |     VARIABLE   TYPE   DESCRIPTION                                                                 |
    |                                                                                                   |
    |     data       list   The imported dataset of the Chicago Bikeshare, a 1551506 x 8 data frame     |
    |                       stored in a list.                                                           |
    |                                                                                                   |
    |     index      int    The desireable column to be selected.                                       |
    |                           0: Start Time                                                           |
    |                           1: End Time                                                             |
    |                           2: Trip Duration                                                        |
    |                           3: Start Station                                                        |
    |                           4: End Station                                                          |
    |                           5: User Type                                                            |
    |                           6: Gender                                                               |
    |                           7: Birth Year                                                           |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |OUTPUT:                                                                                            |
    |                                                                                                   |
    |     VARIABLE      TYPE   DESCRIPTION                                                              |
    |                                                                                                   |
    |     column_list   list   The Selected column from the data input.                                 |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    """
    column_list = []
    # Tip: You can use a for to iterate over the samples, get the feature by index and append into a list
    for i in range(0,len(data)):
        column_list.append(data[i][index])
    return column_list
```
### Task 4
```{py}
# TASK 4
# TO DO: Count each gender. You should not use a function to do that.

gender = column_to_list(data_list, -2) # Selecting the Gender's column of data_list dataframe.

# Lambda Expressions
is_male = lambda x : x == "Male"     # Check each how if the statment is True or False. Later I will coerce
is_female = lambda x : x == "Female" # True to 1 and False to 0 to count the number of each category.
is_blank = lambda x : x == ""        # I used the plt.hist(gender) function to find out the categories of
                                     # Gender's column.

male = sum(list(map(is_male, gender)))        # Applying map() (for each column) and lambdas functions
female = sum(list(map(is_female, gender)))    # I could count the number of each category.
undefined = sum(list(map(is_blank, gender)))  # Obs.: I "coerced" boolean to integer by the using of sum().
```





### Task 5
```{py}
# TASK 5
# TO DO: Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)
def count_gender(data_list):
    """
    -----------------------------------------------------------------------------------------------------
    |DESCRIPTION:                                                                                       |
    |                                                                                                   |
    |     This function counts the number of "Male" and "Female" from the Gender column of the          |
    |     data_list. This is a specific function to be used only to the purpose to calculated the       |
    |     quantity of "Male" and "Female".                                                              |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |INPUT:                                                                                             |
    |                                                                                                   |
    |     VARIABLE   TYPE   DESCRIPTION                                                                 |
    |                                                                                                   |
    |     data_list  list   The list generated after the .read() process. The original file was the     |
    |                       chicago.csv, which has a 1551506 rows and 8 columns.                        |
    |                                                                                                   |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |OUTPUT:                                                                                            |
    |                                                                                                   |
    |     VARIABLE         TYPE   DESCRIPTION                                                           |
    |                                                                                                   |
    |     [male,female]    list   A list of two variables, the first one summarize the number of "Male" |
    |                             the second one summarize the number of "Female".                      |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |REQUIREMENT:                                                                                       |
    |                                                                                                   |
    |     NAME             SCOPE                                                                        |
    |                                                                                                   |
    |     column_to_list   Global                                                                       |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    """
    # Selecting the Gender's column as a local variable.
    local_gender = column_to_list(data_list, -2) # Keep in mind this function has defined in the Task 3.

    # Based on the map() to find True or False and sum() to count.
    male = sum(list(map(lambda x : x == "Male", local_gender)))     # Simplified version, now with one step less
    female = sum(list(map(lambda x : x == "Female", local_gender))) # It's a bit clumsy but understandable.

    return [male, female] # Return of the total number of male and female.
```



### Task 6
```{py}
# TASK 6
# TO DO: Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.
def most_popular_gender(data_list):
    """
    -----------------------------------------------------------------------------------------------------
    |DESCRIPTION:                                                                                       |
    |                                                                                                   |
    |     This function returns which Gender has the majority of in case of the same number returned    |
    |     Equal                                                                                         |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |INPUT:                                                                                             |
    |                                                                                                   |
    |     VARIABLE   TYPE   DESCRIPTION                                                                 |
    |                                                                                                   |
    |     data_list  list   The list generated after the .read() process. The original file was the     |
    |                       chicago.csv, which has a 1551506 rows and 8 columns.                        |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |OUTPUT:                                                                                            |
    |                                                                                                   |
    |     VARIABLE   TYPE   DESCRIPTION                                                                 |
    |                                                                                                   |
    |     answer     str    If the number of "Name" are greater than "Female" return "Male". If the     |
    |                       opposite was true returns "Female". In cases of draw return "Equal".        |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |REQUIREMENT:                                                                                       |
    |                                                                                                   |
    |     NAME             SCOPE                                                                        |
    |                                                                                                   |
    |     count_gender     Global                                                                       |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    """
    # Number of Male and Female calculationg
    local_gender_total = count_gender(data_list) # local_gender_total[0] : Male
                                                 # local_gender_total[1] : Female

    if local_gender_total[0] > local_gender_total[1]:    # Is Male > Female?
        answer = "Male"                                  # If True update answer

    elif local_gender_total[0] == local_gender_total[1]: # Is Male == Female?
        answer = "Equal"                                 # If True update answer

    else:                                                # Is Female > Male
        answer = "Female"                                # If True update answer

    return answer # Return the answer
```



### Task 7
```{py}
# TASK 7
# TO DO: Plot a similar graph for user_types. Make sure the legend is correct.
print("\nTASK 7: Check the chart!")

# Explanation how I conduct this Task.
#
# The print(set(user_types)) give me {'Customer', 'Subscriber', 'Dependent'}, it means the dataframe has
# 3 categories, but with a deeper analisys using a straighfoward plot (plt.hist(quantity)) shows me the
# "Dependent" are exceptions, only 4 instances of this category. For this reason I removed from the graphic
# because it is not a valueable information faced the number of "Customer" and "Subscriber".
#
# If my point of view is not correct, please, let me know. I can fix it and reply you as soon as possible.

# Selecting the desired column
user_types = column_to_list(data_list, -3)

# Selecting the unique categories and removing the "Dependent".
types = list(set(user_types))[0:2]

# Calculating the quantity of each of types ("Customer" and "Subscriber")
quantity = [sum(list(map(lambda x : x == types[0], user_types))),  # Due to the Task 5 requirements my function
            sum(list(map(lambda x : x == types[1], user_types)))]  # count_gender() is very specific and can not
                                                                   # deal with a generic situation like this.

# print(sum(list(map(lambda x : x == "Dependent", user_types)))) # Shows the number of Dependent category.

y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')              # Add the y axis
plt.xlabel('User Types')            # Add the x axis
plt.xticks(y_pos, types)            # Remove x marks
plt.title('Quantity by User Types') # Add Title
plt.show(block=True)
```



### Task 8
```{py}
# TASK 8
# TO DO: Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))

answer = "There are many rows with blank values in gender's column. {} rows with no values"

print("Answer:", answer.format(undefined)) # undefined was calculated in Task 4.
```




### Task 9
```{py}
# TASK 9
# TO DO: Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().

# To be honest, I really do not know what is inside of this set of "ready functions". However, I have tried to
# do an effort to accomplish this task using different ways rather than a simple built-in function.

# Selecting the column of trip duration
trip_duration_list = column_to_list(data_list, 2)

# Defining a lambda expression to coerce str variables to float
conv_to_float = lambda x : float(x) # This is very handy!!

# Converting the elements of trip_duration_list to float
trip_dur_float = list(map(conv_to_float, trip_duration_list))

# Minimum
min_trip = round(sorted(trip_dur_float)[0]) # Could I use .sorted()?

# Maximum
max_trip = round(sorted(trip_dur_float, reverse = True)[0]) # Could I use .sorted()?

# Mean
mean_trip = round(sum(trip_dur_float)/len(trip_dur_float)) # Could I use sum()?

# Median
median_trip = round(sorted(trip_dur_float)[int(len(trip_dur_float)/2)]) # Could I use .sorted()?

# If the use of these built-in function or methods (.sorted(), sum() etc.) is not allowed, I could resubmit the project
# and I will fix it using a loop approach or any other way to calculate those parameters.
```



### Task 10
```{py}
# TASK 10
# Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# TO DO: Check types how many start_stations do we have using set()
user_types = set() # Unique elements

# Selecting the column of Start Stations from data_list
start_stations = column_to_list(data_list, 3)

# First 20 rows to an analysis
# start_stations[0:20]

# Selecting the unique elements of start_stations list.
user_types = list(set(start_stations))
```



### Task 11
```{py}
# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# def new_function(param1: int, param2: str) -> list:
#      """
#      Example function with annotations.
#      Args:
#          param1: The first parameter.
#          param2: The second parameter.
#      Returns:
#          List of X values
#
#      """
```
### Task 12

```{py}
# TASK 12 - Challenge! (Optional)
# TO DO: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it?")
answer = "yes"

def count_items(column_list):
    """
    -----------------------------------------------------------------------------------------------------
    |DESCRIPTION:                                                                                       |
    |                                                                                                   |
    |     This function returns which Gender has majority of in case of the same number returs Equal.   |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |INPUT:                                                                                             |
    |                                                                                                   |
    |     VARIABLE     TYPE   DESCRIPTION                                                               |
    |                                                                                                   |
    |     column_list  list   Is a list with only one variable, this is an output of column_to_list     |
    |                         function.                                                                 |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |OUTPUT:                                                                                            |
    |                                                                                                   |
    |     VARIABLE      TYPE   DESCRIPTION                                                              |
    |                                                                                                   |
    |     item_type     str    Returns all categories in the column_list.                               |
    |                                                                                                   |
    |     count_items   str    Returns the total of each category in item_type.                         |                                                                       |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    """
    # Selecting unique elements from column_list
    item_types = list(set(column_list))

    # Initializing coun_items
    count_items = []

    # Loop to calculated the number each element from item_types
    for i in range(0,len(item_types)):
        count_items.append(sum(list(map(lambda x : x == item_types[i], column_list))))

    return item_types, count_items # Return two lists
```
