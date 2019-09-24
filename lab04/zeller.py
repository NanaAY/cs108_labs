'''A Python program that calculates the day of the week using Zeller's Congruence
Created Spring 2018
lab04
@author: Nana Osei Asiedu Yirenkyi (na29) '''


#Prompt for and read from the user the values of the year, the month and the day of the month
year = int(input('Enter the year:'))

month = int(input('\nEnter the month:'))

day_of_month = int(input('\nEnter the day of the month:'))


#Converts month values 1 and 2 to 13 and 14 respectively
if month == 1:
    month = 13
    year = year -1

elif month == 2:
    month =14
    year = year -1
    

#Computing the day of the week using Zeller's Congruence
day_of_week = (day_of_month + ( ( (month + 1) * 26) // 10) + (year % 100) + ( (year % 100) // 4) + ( (year//100) // 4) + (5 * (year//100) ) ) % 7

days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday' ]

print('\nDay of the week is:', days[day_of_week])