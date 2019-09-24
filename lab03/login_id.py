'''A program for storing a login id
Created February 15, 2018
Lab 03
@author: Toby Sterk (ths6)
@author: Nana Osei (na29)
'''

# Prompt and store the first name
first_name = input("Please enter your first name: ")

# Prompt and store the last name
last_name = input("Please enter your last name: ")
                

# Prompt and store the student ID number
student_number = input("Please enter your student ID number: ")
                     
# Compute login ID
login_ID = first_name[0] + last_name[0:5] + student_number[-2:]
login_ID = login_ID.lower()
# Print login ID
print(login_ID)