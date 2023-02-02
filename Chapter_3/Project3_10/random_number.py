import numpy as np
from math import sqrt
import random

class RandomNumber:
    def __init__(self, p):
        self.p = p
        self.theoretical_mean = p
        self.theoretical_var = p*(1-p)

    def flip(self):
        rn_nb = random.random()
        if rn_nb <= self.p:
            return 1
        else:
            return 0