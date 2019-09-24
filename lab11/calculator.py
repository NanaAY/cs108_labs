'''
Provide calculator functionality
Created Fall 2014
updated, Summer, 2015

@author: smn4
@author: kvlinden
'''
from _hashlib import new

class Calculator:
    
    def __init__(self):
        ''' Initialize calculator memory to 0 '''
        self._memory = 0

    def calculate(self, operand1, operator, operand2):
        ''' Perform the specified calculation '''
        if operand1 == 'M':
            operand1 = self._memory
        elif operand2 == 'M':
            operand2 = self._memory   
        elif operator == '+':
            answer = int(float(operand1)) + int(float(operand2))
        elif operator == '-':
            answer = int(float(operand1)) - int(float(operand2))
        elif operator == 'x':
            answer = int(float(operand1)) * int(float(operand2))
        elif operator == '/':
            answer = int(float(operand1)) / int(float(operand2))
        else:
            raise Exception("INVALID OPERATOR")
        return answer
        
    
        # Implement the calculate function properly.
    
    def get_memory(self):
        return self._memory
    
    
    def set_memory(self,new_memory):
        self._memory = new_memory
        
        
        
if __name__ == '__main__':
    # Do a simple test of 1+1. See the more extensive tests in test.py.
    calc = Calculator()
    print(calc.calculate('0', '+', '1'))
