'''A Python program that computes the wind-chill factor
Created Spring 2018
lab04
@author: Nana Osei Asiedu Yirenkyi (na29) '''



#Prompt for and read from the user the temperature in degrees Fahrenheit called temp and the velocity in m/h
temp = float(input('Enter the temperature in degrees Fahreinheit:'))

velocity = float(input('\nEnter the velocity in miles per hour:'))



#Set temperature between the values of -58F and 41F and velocity above 2m/h
if (temp > 41 or temp < -58) or velocity < 2:
    print("Program can not work. Temp must be between -58F and 41F and velocity can't be less than 2")


#Compute and print wind-chill temperature
else:
    wind_chill = 35.74 + (0.6215 * temp) - (35.75 * (velocity**0.16)) + (0.4275 * temp * (velocity**0.16))
    
    print('\nWind-chill is:', wind_chill)
  
    

#Determining the required number of layers of clothes
if wind_chill < -40:
    print('\nStay at home. ')
elif -40 <= wind_chill < -10:
    print('\nLayers to wear: 4')
elif -10 <= wind_chill < 20:
    print('\nLayers to wear: 3')
elif -20 <= wind_chill < 40:
    print('\nLayers to wear: 2')
elif wind_chill >= 40:
    print('\nLayers to wear: 1')