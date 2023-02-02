from random_number import RandomNumber
from math import sqrt, pi, exp
import numpy as np
from prettytable import PrettyTable
import matplotlib.pyplot as plt


class RandomNumberManager:
    def __init__(self, N, p, nb_trials):
        self.nb_trials = nb_trials
        self.nb_numbers = N
        self.p = p
        self.random_number = RandomNumber(p)
        self.S = [s for s in range(0,N+1)]

        self.theoretical_mean = N*self.random_number.theoretical_mean
        self.theoretical_var = N*self.random_number.theoretical_var
        self.theoretical_sd = sqrt(self.theoretical_var)
        self.theoretical_histogram = self.nb_trials * np.array([(self.combinatorial(self.nb_numbers, s)) * (p ** s) * ((1 - p) ** (self.nb_numbers - s)) for s in range(0, N + 1)])

        self.gaussian_histogram = self.nb_trials * np.array([self.gaussian(s, N) for s in range(0, N + 1)])

        self.mean = 0.0
        self.var = 0.0
        self.sd = 0.0
        self.histogram = np.zeros(self.nb_numbers + 1, int)

        self.do_trials()
        self.calculate()


    def do_trials(self):
        for m in range(self.nb_trials):
            index = 0
            for n in range(self.nb_numbers):
                index += self.random_number.flip()
            self.histogram[index] += 1

    def calculate(self):
        for s in range(self.nb_numbers + 1):
            self.mean += self.histogram[s] * s
        self.mean /= self.nb_trials
        for s in range(self.nb_numbers + 1):
            self.var += self.histogram[s] * (s - self.mean) ** 2
        self.var /= self.nb_trials
        self.sd += sqrt(self.var)


    def print_results(self):
        # Calculate deviations from theory
        mean_dev = round(100 * abs(self.mean - self.theoretical_mean) / self.theoretical_mean, 3)
        var_dev = round(100 * abs(self.var - self.theoretical_var) / self.theoretical_var, 3)
        sd_dev = round(100 * abs(self.sd - self.theoretical_sd) / self.theoretical_sd, 3)
        # Round theoretical and empirical results to 3 decimals
        self.mean = round(self.mean, 3)
        self.var = round(self.var, 3)
        self.sd = round(self.sd, 3)
        self.theoretical_mean = round(self.theoretical_mean, 3)
        self.theoretical_var = round(self.theoretical_var, 3)
        self.theoretical_sd = round(self.theoretical_sd, 3)

        x = PrettyTable()
        x.field_names = ["Theoretical mean", "Empirical mean", "Mean dev (%)"]
        x.add_row([self.theoretical_mean, self.mean, mean_dev])
        print(x)

        y = PrettyTable()
        y.field_names = ["Theoretical var", "Empirical var", "Var dev (%)"]
        y.add_row([self.theoretical_var, self.var, var_dev])
        print(y)

        z = PrettyTable()
        z.field_names = ["Theoretical SD", "Empirical SD", "SD dev (%)"]
        z.add_row([self.theoretical_sd, self.sd, sd_dev])
        print(z)


    def plot_histograms(self):
        plt.subplot(2,1,1)
        plt.scatter(self.S, self.histogram, label='Simulated histogram')
        plt.scatter(self.S, self.theoretical_histogram, label='Theoretical histogram')
        plt.scatter(self.S, self.gaussian_histogram, label='Gaussian histogram')
        plt.title(f'N = {self.nb_numbers}, p = {self.p}. Number of trials = {self.nb_trials}.')
        plt.ylabel("Number of cases")
        plt.legend(loc='upper left')

        deviations1 = np.abs((self.theoretical_histogram - self.histogram))
        deviations2 = np.abs((self.theoretical_histogram - self.gaussian_histogram))

        plt.subplot(2, 1, 2)
        plt.scatter(self.S, deviations1, label='Deviations of simulated data from theory')
        plt.scatter(self.S, deviations2, label='Deviations of gaussian approximation from theory')
        plt.xlabel("s")
        plt.ylabel("Error")
        plt.legend(loc='upper left')

        plt.show()


    def combinatorial(self, N, s):
        return int(self.combinatorial_numerator(N, s) / self.combinatorial_denominator(N, s))

    def combinatorial_numerator(self, N, s):
        if s > 0:
            return (N-s+1)*self.combinatorial_numerator(N, s-1)
        else:
            return 1

    def combinatorial_denominator(self, N, s):
        if s > 0:
            return s*self.combinatorial_denominator(N, s-1)
        else:
            return 1

    def gaussian(self, s, N):
        coeff = 1/(self.theoretical_sd*sqrt(2*pi))
        exponential_num = -(s - self.theoretical_mean)**2
        exponential_den = 2*self.theoretical_var
        exponent = exponential_num/exponential_den
        return coeff*exp(exponent)