'''
Models a problem
Created Fall 2014

@author: na29
'''


class Problem:
    def __init__(self, text=""):
        self.text = text
    
    def get_text(self):
        return self.text