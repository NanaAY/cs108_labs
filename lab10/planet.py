'''
Model a planet
Created Fall 2014

@author: smn4
'''


#gains access to the turtle code
import turtle

class Planet:
    '''Models a Planet
    invariants:
    the radius, mass and distance of a planet from the sun must be positive numbers'''
    
    def __init__(self, name, rad, m, dist, color):
        '''default constructor. Receives the name, radius, mass, distance and color
         and assigns them to instance variables''' 
        
        if (rad > 0) and (m > 0) and (dist > 0): #ensures the invariant
            self._name = name
            self._radius = rad
            self._mass = m
            self._distance = dist
            self._color = color
            self._x = dist
            self._y = 0
            
            #setting up a turtlefor the planet
            self._turtle = turtle.Turtle()
            self._turtle.penup()
            self._turtle.color(self._color) 
            self._turtle.shape('circle')
            self._turtle.shapesize(self._radius, self._radius)
            self._turtle.goto(self._x, self._y)
            
        else:
            raise ValueError('Planet numeric properties must be positive')
            
        
    def get_name(self):
        '''Accesses and returns the name of planet'''
        return self._name
    
    def get_radius(self):
        '''Accesses and returns the radius of planet'''
        return self._radius
    
    def get_mass(self):
        '''Accesses and returns the mass of planet'''
        return self._mass
    
    def get_distance(self):
        '''Accesses and returns the distance of planet from the sun'''
        return self._distance
    
    def set_name(self, newname):
        '''Modifies the name of the Planet'''
        self._name = newname
    
    def __str__(self):
        '''Prints the name of the planet'''
        return self._name
    
    
    
if __name__ == '__main__':   
    
    window = turtle.Screen() #Name the screen where the turtle will appear "window"
    
    print('\t\t\tTESTS............')
    print('\nTesting valid Planets...')
    
    planet1 = Planet('Planet1', 1516, 200000, 45900099,'green') #constructs a planet object
    assert planet1 #ensures the object is valid
    
    planet2 = Planet('Planet2', 3456, 560000, 89900099, 'red') #constructs a planet object
    assert planet2 #ensures the object is valid
    
    print('Passed...') #Output showing that all tests passed
    print('\nTesting invalid Planets...')
    
#     planet3 = Planet('Planet3',0,200000,45900099)   #constructs a planet object
#     assert planet3  #ensures the object is valid
#     
#     planet4 = Planet('Planet4',1516,0,45900099)  #constructs a planet object
#     assert planet4 #ensures the object is valid
#     
#     planet5 = Planet('Planet4',1516,4568,-3)  #constructs a planet object
#     assert planet5 #ensures the object is valid

    # Keep the window open until it is clicked
    window.exitonclick()