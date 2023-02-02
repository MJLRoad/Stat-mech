from math import sqrt
import random as rd

class Dice:
    def __init__(self, S):
        self.sides = S
        self.theoretical_mean = round((S+1)/2, 3)
        self.theoretical_var = round((S**2 - 1)/12, 3)
        self.theoretical_sd = round( sqrt(self.theoretical_var) , 3)

    def roll(self):
        return rd.randint(1, self.sides)