import numpy as np
from random_number_manager import RandomNumberManager
from random_number import RandomNumber

N = 200 #Number of random numbers
mu = 15
p = mu/N
nb_trials = 10000

random_number_manager = RandomNumberManager(N, p, nb_trials)

random_number_manager.print_results1()
random_number_manager.print_results2()
random_number_manager.plot_histograms()