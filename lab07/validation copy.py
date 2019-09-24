'''
Starter code for lab 7 - This program implements a simple text menu user interface.

Created Summer, 2015

@author: kvlinden
''' 

def printMenu():
    '''Print the text menu.'''
    print('\nPlease select from the following list of options (type the appropriate character):')
    print('A. Print a nice message')
    # Add menu options here for three new string tests.
    print('Q. Quit')


# Run the text-menu interface until the user wants to quit.
while True:
    printMenu()
    choice = input('Choice: ').upper()
    
    if choice == 'A':
        print('Have a great day!')
        
    # Add code here to handle tests for the three string types.
    # Each option should read a value from the user, pass it to the appropriate check routine and print the result.
        
    elif choice == 'Q':
        break
   
    else:
        print('I\'m sorry, {0} is not a valid option.'.format(choice))
    
print('\nGood-bye!')

