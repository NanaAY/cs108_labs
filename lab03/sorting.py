'''A program for sorting the items in a list
Created February 15, 2018
Lab 03
@author: Toby Sterk (ths6)
@author: Nana Osei (na29)
'''

# Prompt user for 4 numbers
num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))
num_3 = int(input("Please enter the third number: "))
num_4 = int(input("Please enter the fourth number: "))
# Store the numbers in a list
num_list_unsorted = [num_1, num_2, num_3, num_4]
print(num_list_unsorted)
# Sort the numbers from minimum to maximum
num_list_sorted = []

num_list_sorted.append(min(num_list_unsorted))
num_list_unsorted.remove(min(num_list_unsorted))

num_list_sorted.append(min(num_list_unsorted))
num_list_unsorted.remove(min(num_list_unsorted))

num_list_sorted.append(min(num_list_unsorted))
num_list_unsorted.remove(min(num_list_unsorted))

num_list_sorted.append(min(num_list_unsorted))
num_list_unsorted.remove(min(num_list_unsorted))

# Print the sorted list
print(num_list_sorted)