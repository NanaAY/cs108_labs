'''
Created Spring 2018
lab09
@author: Nana Osei Asiedu Yirenkyi (na29) '''


import sys #Imports the system-specific parameters and functions 
from driver import *  #Gains access to the driver.py code


class Employee(): #class definition
    '''Employee Class
    Invariants:
    Salary is > 20000'''
    
    
    def __init__(self, line= ''):
        
        if line  == '': #sets the default parameters if line is empty
            self._first = 'Ray'
            self._last =  'David'
            self._rank = 'Manager'
            self._salary = 24500
            
        elif line != '': # 
            strings = line.split() #splits the content of line using the whitespaces
            
            if float(strings[3]) >= 20000: #ensures the invariable
                self._first = strings[0]
                self._last =  strings[1]
                self._rank = strings[2]
                self._salary = float(strings[3])
                
            else:
                print('Salary must be above $20000', file=sys.stderr)
                sys.exit(-1)
                        
            
        
    def __str__(self):
        ''' Returns Employee details in appropriate string format '''
        
        return self._last + ', ' + self._first[0]+'. : ' + self._rank + ' ' + '($'+str(self._salary)+')'
    
    
    
    def get_rank(self):
        '''Accesses and returns rank'''
        
        return self._rank
    
    
    
    def get_salary(self):
        '''Accesses and returns salary'''
        
        return self._salary
    
    
                    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MAIN CODE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
                    
#~~~~~~~~~~~~~~~~TESTS~~~~~~~~~~~~~~~~~#
                
if __name__ == '__main__': #checks if the file is being run as a script.
    
    print('\n\t\t\tTesting...')  
    
    default_emp = Employee() #Constructs and prints an employee object with the default values.
    print('\nDefault employee:', default_emp)
    
    test_emp = Employee('first last rank 20500') #Constructs and prints an employee object with the given values.
    print('Test Employee 1:', test_emp)
    
    test_emp2 = Employee('Daniel Ato Captain 30500')  #Constructs and prints an employee object with the given values.
    print('Test Employee 2:', test_emp2)
    
#     test_emp3 = Employee('Chris Atom Captain 3500')
#     print('Test Employee 3:', test_emp3)
     
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    print('\n\t\t\tMain....\n')
    f = open('employee_stats.txt','w') #creates and opens employee_stats.txt write write permissions
    f.write('\tTHIS FILE CONTAINS USEFUL EMPLOYEE STATS\n\nEmployee with the highest pay: \n' + str(max_employee)) #writes the given string to the file
    f.write('\n\nEmployee with the lowest pay: \n' + str(min_employee)) #writes the given string to the file
    print_averages(totals,counts,f) #calls the print_averages functions from driver.py
    f.close() #closes the file
     
     
    

