from dice import Dice
from prettytable import PrettyTable
from math import sqrt
from numpy import zeros

class DiceManager:
    def __init__(self, nb_dices, nb_sides, trials):
        self.nb_dices = nb_dices
        self.sides = nb_sides
        self.trials = trials
        self.trials_results = zeros(self.trials, int)

        self.theoretical_mean = 0.0
        self.theoretical_var = 0.0
        self.theoretical_sd = 0.0

        self.mean = 0.0
        self.var = 0.0
        self.sd = 0.0


    def rolls(self):
        dice = Dice(self.sides)
        self.theoretical_mean += (self.nb_dices)*(dice.theoretical_mean)
        self.theoretical_var += (self.nb_dices)*(dice.theoretical_var)
        self.theoretical_sd += sqrt(self.theoretical_var)
        #Simulate trials
        for i in range(self.trials):
            for j in range(self.nb_dices):
                self.trials_results[i] += dice.roll()
        # Calcule mean, var and sd
        for i in range(self.trials):
            self.mean += self.trials_results[i]
        self.mean /= self.trials

        for i in range(self.trials):
            self.var += (self.trials_results[i]-self.mean)**2
        self.var /= self.trials

        self.sd += sqrt(self.var)


    def print_results(self):
        # Calculate deviations from theory
        # mean_dev = round(100 * abs(self.mean - self.theoretical_mean) / self.theoretical_mean, 3)
        # var_dev = round(100 * abs(self.var - self.theoretical_var) / self.theoretical_var, 3)
        sd_dev = round(100 * abs(self.sd - self.theoretical_sd) / self.theoretical_sd, 3)
        # Round theoretical and empirical results to 3 decimals
        # self.mean = round(self.mean, 3)
        # self.var = round(self.var, 3)
        self.sd = round(self.sd, 3)
        # self.theoretical_mean = round(self.theoretical_mean, 3)
        # self.theoretical_var = round(self.theoretical_var, 3)
        self.theoretical_sd = round(self.theoretical_sd, 3)

        # x = PrettyTable()
        # x.field_names = ["Theoretical mean", "Empirical mean", "Mean dev (%)"]
        # x.add_row([self.theoretical_mean, self.mean, mean_dev])
        # print(x)
        #
        # y = PrettyTable()
        # y.field_names = ["Theoretical var", "Empirical var", "Var dev (%)"]
        # y.add_row([self.theoretical_var, self.var, var_dev])
        # print(y)

        z = PrettyTable()
        z.field_names = ["Theoretical SD", "Empirical SD", "SD dev (%)"]
        z.add_row([self.theoretical_sd, self.sd, sd_dev])
        print(z)