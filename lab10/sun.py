'''
Model a sun
Created Fall 2014

@author: smn4
'''


#gains access to the turtle code
import turtle


class Sun:
    '''Models a Sun
    invariant: the radius and mass should be positive numbers and the temperature should
     also be greater than absolute zero (-273.15°C).'''

    def __init__(self, name, rad, m, temp):
        '''default constructor. Receives the name, radius, mass, temperature
         and assigns them to instance variables''' 
        
        if (rad > 0) and (m > 0) and (temp > -273.15): #ensures the invariant
            self._name = name
            self._radius = rad
            self._mass = m
            self._temp = temp
            self._x = 0
            self._y = 0
            
            #setting up a turtle for the sun
            self._turtle = turtle.Turtle()
            self._turtle.penup()
            self._turtle.color('yellow') 
            self._turtle.shape('circle')
            self._turtle.shapesize(self._radius, self._radius)
            self._turtle.goto(self._x, self._y)
        else:
            raise ValueError('Sun numeric properties must be positive and \ntemperature should also be greater than absolute zero (-273.15°C).')
        
    def get_mass(self):
        '''Accesses and returns the mass of planet'''
        return self._mass
    
    def __str__(self):
        '''Prints the name of the planet'''
        return self._name
    
    
    
    
if __name__ == '__main__':   
    
    print('\t\t\tTESTS............')
    print('\nTesting valid Sun objects...')
    
    sun1 = Sun('Sun1', 6778, 789, 7) #constructs a sun object
    assert sun1 #ensures the object is valid
    
    sun2 = Sun('Sun2', 6532, 897, -200) #constructs a sun object
    assert sun2 #ensures the object is valid
    
    print('Passed...')
    print('\nTesting invalid Sun objects...')
    
#     sun3 = Sun('Sun1', 6778, -9, 7) #constructs a sun object
#     assert sun3 #ensures the object is valid
#     
#     sun4 = Sun('Sun2', 6532, 897, -273.15) #constructs a sun object
#     assert sun4 #ensures the object is valid
#     
#     sun5 = Sun('Sun1', -5, 789, 7) #constructs a sun object
#     assert sun5 #ensures the object is valid