################################################################################
#                                                                              #
#  Author: Anderson Hitoshi Uyekita                                            #
#  Lesson: 05                                                                  #
#  Quiz  : 09                                                                  #
#  Course: Data Science - Foundation I               Cod: nd110                #
#  Date:   06/12/2018                                                          #
#                                                                              #
################################################################################

names =  input("Enter names separated by comas: ")                   # get and process input for a list of names
assignments =  input("Enter assignment counts separated by comas: ") # get and process input for a list of the number of assignments
grades =  input("Enter grades separated by comas: ")                 # get and process input for a list of grades

names = names.split(',')             # Split the string into elements
assignments = assignments.split(',') # Split the string into elements
grades = grades.split(',')           # Split the string into elements

all_data = zip(names,assignments,grades)

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for names,assignments,grades in all_data:
    print(message.format(names,assignments,grades,str(int(grades) + 5))) # Potencial grade is equal "grades + 5"
