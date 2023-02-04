import numpy as np
import random as rd
from prettytable import PrettyTable

class Die:
    def __init__(self, nb_trials, nb_sides):
        self.trials = nb_trials
        self.sides = nb_sides
        self.histogram = np.zeros(self.sides, int)

    def throw(self):
        for i in range(self.trials):
            random_side = int((rd.random()) * self.sides)
            self.histogram[random_side] += 1

    def print_results(self):
        x = PrettyTable()
        x.field_names = ["Side", "Histogram", "Histogram - trials/sides"]
        for s in range(self.sides):
            x.add_row([s + 1, self.histogram[s], int(self.histogram[s] - self.trials / self.sides)])
        print(x)