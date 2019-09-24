'''
Models a True False Question
Created Spring 2018

@author: na29
'''

# class Problem:
#     def __init__(self, text=""):
#         self.text = text
# 
#     def get_text(self):
#         return self.text


from problem import *


class TrueFalse(Problem):
    ''' Model a short-answer question '''
    
    def __init__(self, q, a):
        ''' Construct a short-answer question with question and answer texts '''
        
        Problem.__init__(self, q)
        if isinstance(a, bool):
            self.answer = a
        else:
            raise TypeError('Should be a boolean value')
        
    def ask_question(self):
        ''' Return the question text '''
        return super().get_text()+'\nIs this statement true or false?'
    
    
    def check_answer(self, a):
        ''' Return True if a is the correct answer; False otherwise '''
        return self.answer == a 
    
    
    def get_answer(self):
        ''' Return the answer text '''
        return str(self.answer)
    
    
if __name__ == "__main__":
    q = TrueFalse('question', 'answer')
    assert q.get_text() == 'question'
    assert q.get_answer() == 'answer'
    assert q.ask_question() == 'question?'
    assert not (q.check_answer('ans'))
    assert q.check_answer('answer')
    print('All ShortAnswer tests passed!')