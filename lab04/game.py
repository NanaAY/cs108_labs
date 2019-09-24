'''A Python program that simulates the rock, paper, scissors game
Created Spring 2018
lab04
@author: Nana Osei Asiedu Yirenkyi (na29) '''


from random import randint



#Prompt for and read from the user the values of rock, paper or scissors
user_choice = int(input('Enter 0 for rock, 1 for paper or 2 for scissors: '))

if user_choice > 2 or user_choice < 0:
    print('\nWrong Value entered.')


computer_choice = randint(0,2)  #sets the computer's choice to any random number between 0 and 2


#Determining the winner
if user_choice == 0:
    if computer_choice == 1:
        print('\nComputer wins!')
    elif computer_choice == 2:
        print('\nYou win!')
    else:
        print("It's a draw!")


elif user_choice == 1:
    if computer_choice == 0:
        print('\nYou win!')
    elif computer_choice == 2:
        print('Computer wins!')
    else:
        print("\nIt's a draw!")

elif user_choice == 2:
    if computer_choice == 0:
        print('\nComputer wins!')
    elif computer_choice == 1:
        print('You win!')
    else:
        print("\nIt's a draw!")



