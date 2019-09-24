'''
Created Spring 2018
lab08
@author: Nana Osei Asiedu Yirenkyi (na29) '''



import sys #Imports the system-specific parameters and functions 


def computeGCD(alpha, beta):
    '''
    (int, int) -> int
    This function finds the greatest common divisor of two integers, using
    Euclid's algorithm
    '''
    alpha = abs(alpha)
    beta = abs(beta)
    remainder = alpha % beta
    while (remainder != 0):
        alpha = beta
        beta = remainder
        remainder = alpha % beta
    return beta



class Fraction():
    '''Fraction Class 
    Invariable: a fraction object must have a denominator that is not zero.'''
    
    def __init__(self, numerator= 0, denominator= 1):
        '''This initializes a fraction object with default values 0 and 1 for the numerator and denominator respectively,
        receives values for the numerator and denominator and checks if these values satisfy the invariant.
        and checks '''
        if denominator != 0: #ensures denominator is not zero
            self._numerator = numerator
            self._denominator = denominator
            self.simplify() # This simplifies the values provided by the calling program.
        else:
            print('Unable to create valid fraction', file=sys.stderr)
            sys.exit(-1)
    
    
    
    
    def __str__(self):
        '''Returns Fraction in string format'''
        
        return str(self._numerator) + '/' +  str(self._denominator)
    
    
    
    def get_numerator(self):
        '''accesses and returns the value of the numerator'''
        
        return self._numerator
    
    
    def get_denominator(self):
        '''accesses and returns the value of the numerator'''
        
        return self._denominator
    
    
    def simplify(self):
        '''This method modifies the fraction by simplifying it using the gcd of the numerator and denominator'''
        
        gcd =computeGCD(self._numerator, self._denominator)
        
        if gcd != 0:
            self._numerator = (self._numerator//gcd)
            self._denominator = (self._denominator//gcd)
            
        if self._denominator < 0:
            self._numerator *= -1
            self._denominator *= -1
            
            
    def __mul__(self, other):
        '''This method receives a fraction object 'other' by which to multiply with self.'''
        if other.get_denominator !=0:
            new_numerator = self._numerator * other.get_numerator()
            new_denominator = self._denominator * other.get_denominator()
            new_fraction = str(new_numerator) + '/' +  str(new_denominator)
            self.simplify()
            return new_fraction
        else:
            print('Unable to create valid fraction', file=sys.stderr)
            sys.exit(-1)
            
        
        
            
            







































                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TESTS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


f1 = Fraction() #Construct a fraction object with the default values.
print('f1:',f1) #Print the object.


f2 = Fraction(1, 2)     #Construct a fraction object for one half.
print('f2:',f2)               #Print the object.


        #Exercise 8.4
# f_3 = Fraction(0,0)
# print('f_3:',f_3)

# f_4 = Fraction(10,0)
# print('f_4:',f_4)


f_5 = Fraction(17,3)
print('f_5:',f_5)


        #Test accessor method
print('f_5 denominator:', f_5.get_denominator())
print('f_5 numerator:', f_5.get_numerator())


f3 = Fraction(2, 4)     # Construct a fraction object for two fourths.
print('f3 simplified:',f3)     # Print the object


        #Exercise 8.6
f_6 = Fraction(12,4)
print('f_6 simplified:',f_6)

f_7 = Fraction(-4,-1)
print('f_7 simplified:',f_7)

f_8 = Fraction(-8,-8)
print('f_8 simplified:',f_8)


        #Exercise 8.7
f_9 = f1 * f2
print('f1 * f2:', f_9)

f_10 = f_5 * f_6
print('f_5 * f_6:',f_10)

f_11 = f_7 * f2
print('f_7 * f2:',f_11)
