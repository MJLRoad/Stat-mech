# ---------------------------- DESCRIPTION ------------------------------- #
"""
In this project, a random integer is chosen between 1 and nb_sides, its value is recorded, and
the process is repeated nb_trials times. Then, the histogram (the number
of times each integer occurred), is printed out, and the program tells you how
many seconds the program took, and quits.
"""

from die import Die
from clock import now

print("This program can create a die with an arbitrary number of sides")
nb_sides = int(input("How many sides do you want for your die? "))
print("This program can also throw the die a number of times")
nb_trials = int(input("How many trials do you want this program to carry out?"))

t0 = now()

die = Die(nb_trials, nb_sides)
die.throw()
die.print_results()

t1 = now()
print(f"Program time: {t1 - t0}")