'''
GUI controller for a particle simulation
Created Fall 2014
Updated Summer, 2015

@author: smn4
@author: kvlinden
@author: Nana Osei Asiedu Yirenkyi (na29)
'''

from tkinter import *
from random import randint
from particle import *
from helpers import *

class ParticleSimulation:
    ''' Creates particle simulator '''
    
    def __init__(self, window):
        ''' Construct the particle simulator GUI '''
        self.window = window
        self.window.protocol('WM_DELETE_WINDOW', self.safe_exit)
        self.width = 400
        self.canvas = Canvas(self.window, bg='black',
                        width=self.width, height=self.width)
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self.check_remove_particle)
        add_particle_button = Button(self.window, text='Add Particle', command=self.add_button)
        add_particle_button.pack()
        self.terminated = False
        self.p_list = []
#         self.paddle1 = Paddle(tag='Paddle1')
#         self.paddle2 = Paddle(325, 10, color= 'blue', tag='Paddle2')
        self.render()
#         self.render_paddle()
        
        
    def render(self):
        '''This method makes a particle appear to move around the screen'''
        if self.terminated == False:
            self.canvas.delete(ALL)
            for particle in self.p_list:
                particle.move(self.canvas)
                particle.render(self.canvas)
                for particle2 in self.p_list:
                    particle.bounce(particle2)
            self.canvas.after(20, self.render)
            self.canvas.update()
        
#     def render_paddle(self):
#         '''This method makes the kingpong appear to move around the screen'''
#          
#         if self.terminated == False:
#             self.canvas.delete(ALL) #MIGHT WANT TO DELETE ONLY PADDLE
#             self.paddle1.render(self.canvas)
#             self.paddle2.render(self.canvas)
#         self.canvas.after(1, self.render_paddle)
        
    def safe_exit(self):
        ''' Turn off the event loop before closing the GUI '''
        self.terminated = True
        self.window.destroy()
        
    def add_button(self):
        '''This method adds a new particle when the add button is clicked'''
        new_particle = Particle(randint(0,self.width), randint(0,self.width),
                                 randint(-25,25), randint(-25,25))
        self.p_list.append(new_particle)
        
    def check_remove_particle(self, event):
        '''This method removes a particle when it is clicked upon'''
        for particle in self.p_list[:]:
            if ( ( (event.x - particle.get_x() ) ** 2)
                  + ( (event.y - particle.get_y() ) ** 2) ) ** 0.5 < particle.get_radius():
                self.p_list.remove(particle)
        


if __name__ == '__main__':
    root = Tk()
    root.title('Particle Simulation')    
    app = ParticleSimulation(root)
    root.mainloop()
    
