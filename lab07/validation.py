'''This program deals with the validation of user inputed strings
Created Spring 2018
lab07
@author: Nana Osei Asiedu Yirenkyi(na29)'''


def printMenu():
    '''Print the text menu.'''
    print('\nPlease select from the following list of options (type the appropriate character):')
    print('A. Print a nice message')
    print('S. Social Security Validation')
    print('P. Password Validation')
    print('C. Credit Card Validation')
    print('Q. Quit')


def isValidSSN(ssn):
    '''Receives a SSN string and determines whether or not it is properly formatted'''
    if len(ssn) != 11 or (ssn[3] != '-' and ssn[6] != '-'): #ensure the ssn has 11 characters and that the 4th and 7th characters are hyphens
        return 'Invalid SSN'
    elif (ssn[0:2].isdigit() == False) or (ssn[4:5].isdigit() == False) or (ssn[7:10].isdigit() == False): #ensures that the first 3, middle 2 and last 4 characters are digits
        return 'Invalid SSN'
    else:
        return 'Valid SSN'


def isValidPassword(password):
    '''Receives a string and checks whether a given string is a valid password'''
    digits = 0 #keeps count of the number of digits in the password
    for char in password:
        if char.isdigit() == True:
            digits += 1
    if (digits < 2) or len(password) < 8 or (password.isalpha() == True): #ensures that the password has atleast 2 digits, is alphanumeric and has more than 8 characters
        return 'Invalid Password' 
    else:
        return 'Valid Password' 
  
    
def isValidPrefix(card_num):
    '''Checks the validity of the first character(s) of the card number and returns False if invalid'''
    if card_num.startswith('37') == True:
        return 'Valid: American Express'
    elif card_num.startswith('4') == True:
        return 'Valid: Visa'
    elif card_num.startswith('5') == True:
        return 'Valid: MasterCard'
    elif card_num.startswith('6') == True :
        return 'Valid: Discover'
    else:
        return False
    
    
def sum_of_odds(card_num):
    '''Adds together all digits in the odd places from right to left in the card number string
    and returns the sum'''
    odds_from_right = card_num[-1::-2] #finds the numbers in odd places from the right
    list_of_odds =[]
    for num in odds_from_right:
        odd = int(num)
        list_of_odds.append(odd)
    return (sum(list_of_odds))   #returns the sum of odds


def sum_of_double_evens(card_num):
    '''Doubles every second digit from right-to-left and returns the sum of those digits'''
    evens_from_right = card_num[-2::-2] #finds the numbers in even places from the right
    double_evens = []
    for num in evens_from_right:
        double = int(num) *2 #doubles the numbers found
        double_evens.append(double)
    for number in double_evens:
        if number > 9: #checks for numbers with more than one digit and adds both digits
            double_evens.remove(number)
            number = str(number)
            digit1 = number[0]
            digit2 = number[1]
            summ = int(digit1) + int(digit2)
            double_evens.append(summ)
    return(sum(double_evens)) #returns the sum


def isValidCC(card_num):
    '''Receives a credit card number string and then checks the validity of the number.'''
    if (isValidPrefix(card_num) != False) and (13 <= len(card_num) <= 16) and (card_num.isdigit() == True) and ((sum_of_double_evens(card_num) + sum_of_odds(card_num))%10 == 0):
        return '\nValid Credit Card'
    else:
        return '\nInvalid Credit Card'

        
          
        
          
# Run the text-menu interface until the user wants to quit.
while True:
    printMenu()
    choice = input('Choice: ').upper()
    
    if choice == 'A':
        print('Have a great day!')
    elif choice == 'S':
        ssn_number = input('\nEnter a Social Security Number:')
        print(isValidSSN(ssn_number))
    elif choice == 'P':
        user_password = input('\nEnter a Password:')
        print(isValidPassword(user_password))
    elif choice == 'C':
        credit_card_number = input('\nEnter a credit card number:')
        print(isValidCC(credit_card_number))     
    elif choice == 'Q':
        break
    else:
        print('I\'m sorry, {0} is not a valid option.'.format(choice))
    
print('\nGood-bye!')


