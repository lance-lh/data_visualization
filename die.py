from random import randint

class Die():
    '''a class represented dice'''

    def __init__(self,num_sides=6):
        '''dice has 6 sides'''
        self.num_sides = num_sides

    def roll(self):
        '''return a random value within [1,6]'''
        return randint(1,self.num_sides)