'''
Model of a solar system
Created Fall 2014

@author: smn4
'''
#gains access to all code from sun.py and planet.py
from sun import *
from planet import *


class Solar_System:
    '''Models a Solar system'''
    
    def __init__(self):
        self._sun = None
        self._planets = []
        
    def add_sun(self, a_sun):
        '''Receives a sun object and assigns it to self._sun if the object is valid'''
        
        if isinstance(a_sun, Sun): #ensures the object is valid
            self._sun = a_sun
        else:
            raise TypeError('add_sun(): cannot add ' + str(type(a_sun)) + ' to solar system')

        
    def add_planet(self, a_planet):
        '''Receives a planet object and adds it to the list of planets if the object is valid'''
        
        if isinstance(a_planet, Planet): #ensures the object is valid
            self._planets.append(a_planet)
        else:
            raise TypeError('add_planet(): cannot add' + str(type(a_planet)) + ' to solar system')
        
    def show_planets(self):
        '''Prints the list of planets'''
        for a_planet in self._planets:
            print(a_planet)
        
        
        
if __name__ == '__main__':   
     
    print('\t\t\tTESTS............')
    print('\nTesting valid Solar System...')
    
    sun1 = Sun('Sun1', 6778, 789, 7) #constructs a sun object
    planet1 = Planet('Planet1',1516,200000,45900099) #constructs a planet object
    
    sun2 = Sun('Sun2', 6532, 897, -200) #constructs a sun object
    planet2 = Planet('Planet2',3456,560000,89900099) #constructs a planet object
     
    solar_system1 = Solar_System() #constructs a solar system object
    solar_system1.add_planet(planet1) #adds planet 1
    solar_system1.add_sun(sun1)  #adds sun 1
#     solar_system1.show_planets()
    assert solar_system1 #ensures this object is valid
    
    solar_system2 = Solar_System() #constructs a solar system object
    solar_system2.add_planet(planet2) #adds planet 2
    solar_system2.add_sun(sun2) #adds sun 2
#     solar_system2.show_planets()
    assert solar_system2 #ensures this object is valid
    
    
    
    print('Passed...')
    print('\nTesting invalid Sun objects...')