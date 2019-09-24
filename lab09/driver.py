'''
Created Spring 2018
lab09
@author: Nana Osei Asiedu Yirenkyi (na29) '''


from employee import Employee #Gains access to the Employee Class from employee.py

employees = [] #creates a variable called employees and assigns it to an empty list

with open('employees.txt', 'r') as myfile: #opens and reads the contents of employees.txt
    
    lines = myfile.readlines()
    
    for line in lines: #iterates through the each line of text and appends the different employee details to the empty list
        employees.append(Employee(line))

print('Number of employees:', len(employees)) #prints number of employees

if len(employees) == 0: 
    print('There are no employees')

elif len(employees) > 0: 
    totals = {} #creates 'totals' and assigns it to an empty dictionary
    counts = {} #creates 'counts' and assigns it to an empty dictionary
    max_employee = employees[0] #sets the maximum employee to the first employee in the list
    min_employee = employees[0] #sets the minimum employee to the first employee in the list
    
for employee in employees: #iterates through the list of employees
    if (employee.get_rank() in totals) or (employee.get_rank() in counts): #checks if the employee rank is already a key in the totals or counts dictionaries 
        totals[employee.get_rank()] += employee.get_salary() #accumulates the salaries
        counts[employee.get_rank()] += 1 #increments the count by 1
        
    else: #if the employee rank is not a key in the totals or counts dictionaries, it assigns it
        totals[employee.get_rank()] = employee.get_salary() 
        counts[employee.get_rank()] = 1
        
    if employee.get_salary() > max_employee.get_salary(): #if the current employee salary is greater than the max salary, sets the max salary to the current employee
        max_employee = employee
        
    elif employee.get_salary() < min_employee.get_salary(): #if the current employee salary is less than the min salary, sets the min salary to the current employee
        min_employee = employee
        
        
        
        
def print_averages(total_salaries, total_number,outFile):  #function defition for printing avg salary
    '''receives three parameters, calculates and writes the average to a specified
    file.'''
    
    outFile.write('\n\nRank\tAverage Salary\n')
    for rank in total_salaries:
        avg_salary = total_salaries[rank]/total_number[rank]
        outFile.write(rank +'\t' + str(avg_salary) +'\n')
        
    
    
    
         
        
        
    
       
    