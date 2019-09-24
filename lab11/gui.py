'''Graphical User Interface for the calculator Program
Created Spring 2018
lab11
@author: Nana Osei Asiedu Yirenkyi (na29) & Joshua maher(jdm47)
'''


from tkinter import *
from calculator import *


class Gui:
    '''Gui Class'''
    def __init__(self, window):
        '''constructor that receives a window object from its calling program
         and then creates and places widgets on that window '''
        
        self._calc = Calculator() #Creates an instance variable for the calculator object.
        self._operator = StringVar()
        self._operator.set('+')
        self._result = StringVar()
        self._input1 = StringVar()
        self._input2 = StringVar()
        self._message = StringVar()
        self._message.set('Come on! Let’s calculate!')
        self._memory = StringVar()
        self._memory.set(self._calc.get_memory())
        
        #label and entry for the first number to be entered.
        input1_label = Label(window, text="Input 1:")
        input1_label.grid(row=0, column=0, sticky=E)
        input1_entry = Entry(window, width=6, textvariable =self._input1)
        input1_entry.grid(row=0, column=1, sticky=W)
        
        #label and entry for the second number to be entered.
        input2_label = Label(window, text='Input 2:')
        input2_label.grid(row=1, column=0, sticky=E)
        input2_entry = Entry(window, width=6, textvariable =self._input2)
        input2_entry.grid(row=1, column=1, sticky=W)
        
        operator_frame = Frame(window)
        operator_frame.grid(row=2, column=0, columnspan=2)
        
        #Creates new Buttons for the addition, subtraction, multiplication and division operations and attach them to the frame on the left side.
        add_button = Radiobutton(operator_frame, text="+", variable=self._operator, value='+')
        add_button.pack(side=LEFT)
        add_button = Radiobutton(operator_frame, text="-", variable=self._operator, value='-')
        add_button.pack(side=LEFT)
        add_button = Radiobutton(operator_frame, text="x", variable=self._operator, value='*')
        add_button.pack(side=LEFT)
        add_button = Radiobutton(operator_frame, text="/", variable=self._operator, value='/')
        add_button.pack(side=LEFT)
        
        #Creates a button in the main window to perform the calculation and put it in the fourth row, first column.
        calculate_button = Button(window, text='Calculate', command=self.do_calculation)
        calculate_button.grid(row=4, column=1, sticky=E)
        
        memory_button = Button(window, text='Save Result', command=self.save_result)
        memory_button.grid(row=6, column=0, sticky=E)
            
        
        #creating a result label and put it in the fourth row, first column.
        self.result_label = Label(window, textvariable=self._result, width=6)
        self.result_label.grid(row=4, column=2, sticky=W)
        
        welcome_label = Label(window, textvariable= self._message, width= 20)
        welcome_label.grid(row=5, column=0, columnspan=10, sticky=E)
        
        memory_label = Label(window, textvariable= self._memory, width= 20)
        memory_label.grid(row=6, column=1, columnspan=10, sticky=E)
    
    def do_calculation(self):
        try:
            if (self._input1.get().isdigit() == True) or (self._input2.get().isdigit() == True):
                result = self._calc.calculate(self._input1.get(), self._operator.get(), self._input2.get())
                self._result.set(result)
                self._message.set('Come on! Let’s calculate!')
            else:
                raise ValueError
        except ValueError:
            self._message.set('Invalid Value')
        
    def save_result(self):
        memory = self._calc.set_memory(self._result)   
        self._memory.set(memory) 
        





























#                DRIVER  SCRIPT
if __name__ == '__main__':
    root = Tk()
    root.title('Calculator')
    app = Gui(root)
    root.mainloop()
