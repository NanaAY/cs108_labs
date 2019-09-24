# print(True or False)
# 
# i = [1, 2,3,4]
# 
# for a in range(len(i)):
#     product = i[a]*i[a+1]
#     product *= product
#     print(product)
# import random
# hand1 = []
# hand2 = []
# suits = ['S','D','H','C']
# 
# for i in range(0,5):
#     hand1.append(random.choice(suits))
#     hand2.append(random.choice(suits))
#     
# print('\nHand1:', hand1)
# print('Hand2:', hand2)

# line ='Salary must be above $20000'
# strings = line.split()
# print(strings)
# print(strings[4])

# import employee

# import sys
# 
# class Employee:
#     def __init__(self, line=''):
#         if line == '':
#             self._first = "John"
#             self._last = "Doe"
#             self._rank = "associate"
#             self._salary = 50000
#         if line != '':
#             string = line.split(" ")
#             self._first = string[0]
#             self._last = string[1]
#             self._rank = string[2]
#             self._salary = int(string[3])
#             if self._salary < 20000:
#                 print('Salary must be greater then 20000', file=sys.stderr)
#                 sys.exit(-1)
# 
#     def __str__(self):
#         return '{}, {}.: {} (${})'.format(self._last, self._first[0], self._rank, self._salary)
# 
#     def get_rank(self):
#         return self._rank
# 
#     def get_salary(self):
#         return int(self._salary)
# 
# #                 --------------------------------------------------------------------------------
# 
# 
# employee_list = []
# 
# 
# def print_averages(totals_salary, total_employees, outFile):
#     outFile.write('Rank\tAverage Salary\n')
#     # for each rank in totals
#     print(totals)
#     print(total_employees)
#     for rank in totals:
#         average = totals_salary[rank] / total_employees[rank]
#         outFile.write("%s\t%d\n" % (rank, average))
# with open('employee.txt') as file:
#     line = file.readline()
#     while line != '':
#         employee = Employee(line)
#         employee_list.append(employee)
#         line = file.readline()
#     print(employee_list)
# if len(employee_list) < 1:
#     print("No employees found")
# if len(employee_list) > 0:
#     totals = {}
#     counts = {}
#     max_employee = employee_list[0].get_salary()
#     min_employee = employee_list[0].get_salary()
#     for employee in employee_list:
#         if employee.get_rank() in totals:  # Rank in the dictionary
#             totals[employee.get_rank()] = employee.get_salary()
#             counts[employee.get_rank()] += 1
#         else:  # Rank not on the dictionary
#             totals[employee.get_rank()] = employee.get_salary()
#             counts[employee.get_rank()] = 1
# 
#         if employee.get_salary() > max_employee:
#             max_employee = employee.get_salary()
#         if employee.get_salary() < min_employee:
#             min_employee = employee.get_salary()
# 
#     print("Min --> %d \nMax --> %s" % (min_employee, max_employee))
#     print('%s\n%s' % (totals, counts))
#     print("Starting Right Now")
#     print(max_employee)
#     print(min_employee)
#     stats_file = open('employee_stats.txt', 'w')
#     stats_file.write("Employee earning the most ----> %s\nEmployee earning the lest ---> %s\n" % (str(max_employee), str(min_employee)))
#     print_averages(totals, counts, stats_file)
#     stats_file.close()

# import turtle
# 
# # Changes the turtle name and sets up window
# bob = turtle.Turtle()
# window = turtle.Screen()
# 
# # Asks user for file that contains directions
# direction_file = input("Enter filename containing turtle directions: ")
# 
# with open(direction_file) as file:
#     line = file.readline()
#     while line != '':
#         if "pendown" in line:
#             bob.pendown()
#         if "penup" in line:
#             bob.penup()
#         if "color" in line:
#             strip_spaces = str.strip(line)  # Gets rid of spaces in the beginning and end
#             values = strip_spaces.split(' ')  # Splits the color from the 'color'
#             color = values[1]
#             bob.color(color)  # Sets color to the first index on list
#             bob.goto(50, 50)  # Runs the turtle
#         if "goto" in line:
#             strip_spaces = str.strip(line)  # Gets rid of spaces in the beginning and end
#             values = strip_spaces.split(' ')  # Splits the color from the 'color'
#             x = int(values[1])
#             y = int(values[2])
#             bob.goto(x, y)  # Runs the turtle
#         if "point" in line:
#             strip_spaces = str.strip(line)  # Gets rid of spaces in the beginning and end
#             values = strip_spaces.split(' ')  # Splits the color from the 'color'
#             size = int(values[1])  # Sets size to the first index on list
#             bob.dot(size)  # Runs the turtle
#         if line.startswith("#"):
#             strip_spaces = str.strip(line)  # Gets rid of spaces in the beginning and end
#             print(line[0], line[2:])  # Runs the turtle
#         line = file.readline()  # reads the next line
# window.exitonclick()

user_input = ''
while user_input != 'q':
    try:
        weight = int(input("Enter weight (in pounds): "))
        height = int(input("Enter height (in inches): "))

        bmi = (float(weight) / float(height * height)) * 703
        print('BMI:', bmi)
        print('(CDC: 18.6-24.9 normal)\n')  # Source www.cdc.gov
    except:
        print('Could not calculate health info.\n')

    user_input = input("Enter any key ('q' to quit): ")