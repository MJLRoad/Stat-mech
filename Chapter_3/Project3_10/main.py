import numpy as np
from random_number_manager import RandomNumberManager
from random_number import RandomNumber

N = 30 #Number of random numbers
p = 0.85 #probability of Fj = 1
nb_trials = 10000

random_number_manager = RandomNumberManager(N, p, nb_trials)

random_number_manager.print_results()
random_number_manager.plot_histograms()