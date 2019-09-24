'''
Model a single particle
Created Fall 2014
Updated Summer, 2015

@author: smn4
@author: kvlinden
'''

class Particle:
    '''
    Particle models a single particle that may be rendered to a canvas
    '''

    def __init__(self, x = 50, y = 50, velX = 10, velY = 15, radius = 15, color = '#663977'):
        '''
        Constructor
        '''
        self._x = x
        self._y = y
        self._velX = velX
        self._velY = velY
        self._radius = radius
        self._color = color
        
    def render(self, canvas):
        '''A method that receives a canvas and uses the canvas and 
        instance variables to draw a circular representation of the particle.'''
        canvas.create_oval(self._x - self._radius,
                           self._y - self._radius,
                           self._x + self._radius,
                           self._y + self._radius,
                           fill = self._color)
    def move(self, canvas):
        self._x += self._velX
        self._y += self._velY
        if ( (self._x + self._radius > canvas.winfo_reqwidth() and self._velX > 0),
              or (self._x - self._radius < canvas.winfo_reqwidth()) ):