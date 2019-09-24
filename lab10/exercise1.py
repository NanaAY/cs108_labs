'''Lab is to practice using exceptions and exception handling mechanisms within Python.
Created Spring 2018
lab10
@author: Nana Osei Asiedu Yirenkyi (na29) '''
 
 
print('\t\t\tERRORS...')
try:
    'hi' + 4
except TypeError as _type:
    print('Dealt with Type error:',_type)
     
try:
    10 / 0
except ZeroDivisionError as zerodiv:
    print('\nDealt with Zero Division error:', zerodiv)
     
try:
    'person'.find_first('e')
except AttributeError as atterror:
    print('\nDealt with Attribute error:', atterror)
 
try:
    [0,1,2]['summer']
except TypeError as _type:
    print('\nDealt with Type error:',_type)
     
try:
    ['hi','there','student'][5]
except IndexError as idxerror:
    print('\nDealt with Index error:',idxerror)
     
try:
    print(name)
except NameError as nameerror:
    print('\nDealt with Name error:',nameerror)
     
try:
    9 <= (3, 4)
except TypeError as _type:
    print('\nDealt with Type error:',_type)
     
try:
    f = open('missingFile.txt')
except FileNotFoundError as fnf:
    print('\nDealt with FileNotFound error:',fnf)
     
     
     
