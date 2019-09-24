''' This program determines the four perfect numbers between 1 and 1000
Created Spring 2018
lab05
@author: Nana Osei Asiedu Yirenkyi (na29) & Joshua maher(jdm47)
'''
print('This program determines the perfect numbers from 2 to 10000.')

num_perfect = 0 #Initializes a variable called 'num_perfect' to keep track of the number of perfect numbers.

#Iterating a loop from 2 to 10000
for value in range(2, 10001):

    low = 1

    high = value

    divisors = []#creates an empty list called 'divisors'.

#Determining the divisors of the values from 2 to 10000
    while low < high:
        if (value % low) == 0:
            high = (value / low)
            divisors.append(low)
            if high != low:
                divisors.append(high)
        low += 1
    
    #Removing 'value' from the list and finding the sum of the other values of the list.
    divisors.remove(value)  
    summ = sum(divisors)
    
    perfect = []#Creates an empty list called 'perfect_num'

#Determining the four perfect numbers
    if summ == value:
        perfect.append(value) #Adds the found perfect numbers to the perfect_num list 
        num_perfect += 1
        print(perfect,end=' ')
    if num_perfect == 4:
        print('\nYou found the four perfect numbers!')
        break


