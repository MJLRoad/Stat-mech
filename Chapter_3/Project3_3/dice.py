from math import sqrt
from prettytable import PrettyTable
import random as rd
from numpy import zeros

class Dice:
    def __init__(self, S, N):
        self.sides = S
        self.theoretical_mean = round((S+1)/2, 3)
        self.theoretical_var = round((S**2 - 1)/12, 3)
        self.theoretical_sd = round( sqrt(self.theoretical_var) , 3)

        self.trials = N
        self.histogram = zeros(self.sides, int)
        self.mean = 0.0
        self.var = 0.0
        self.sd = 0.0

    def roll(self):
        print(f"Number of sides = {self.sides}")
        print(f"Number of trials = {self.trials}")
        print("Rolling dice...")
        for i in range(self.trials):
            random_side = rd.randint(0, self.sides - 1)
            self.histogram[random_side] += 1

        for n in range(self.sides):
            self.mean += (n+1)*self.histogram[n]
        self.mean /= self.trials

        for n in range(self.sides):
            self.var += (self.histogram[n])*((n+1) - self.mean)**2
        self.var /= self.trials

        self.sd += sqrt(self.var)


    def print_results(self):
        x = PrettyTable()
        #Deviation from theory (%)
        x.field_names = ["Theoretical mean", "Mean dev (%)", "Theoretical variance", "Variance dev (%)", "SD", "SD dev (%)"]
        mean_dev = round( 100*abs(self.mean - self.theoretical_mean)/self.theoretical_mean, 3)
        var_dev = round( 100*abs(self.var - self.theoretical_var)/self.theoretical_var, 3)
        sd_dev = round( 100*abs(self.sd - self.theoretical_sd)/self.theoretical_sd, 3)
        x.add_row([self.theoretical_mean, mean_dev, self.theoretical_var, var_dev, self.theoretical_sd, sd_dev])
        print(x)