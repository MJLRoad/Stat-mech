import numpy as np
import random as rd
from prettytable import PrettyTable

class Die:
    def __init__(self, nb_trials, nb_sides):
        self.trials = nb_trials
        self.sides = nb_sides
        self.histogram = np.zeros(self.sides, int)

    def throw(self):
        print(f"Number of trials: {self.trials}")
        for i in range(self.trials):
            random_side = int((rd.random()) * self.sides)
            self.histogram[random_side] += 1

    def print_results(self):
        x = PrettyTable()
        x.field_names = ["Side",  "Histogram",  "Histogram deviation",  "Frequency",  "Frequency deviation"]
        for s in range(self.sides):
            side = s + 1
            hist = self.histogram[s]
            hist_dev = int(abs(hist - self.trials / self.sides))
            freq = round(hist / self.trials, 5)
            freq_dev = round(abs(freq - 1 / self.sides),5)
            x.add_row([side, hist, hist_dev, freq, freq_dev])
        print(x)