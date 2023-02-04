# ---------------------------- PROBLEM 3.1 STATEMENT ------------------------------- #
"""
ROLLING A DIE WITH A COMPUTER
For this problem, either modify the Python's Project3_0,
or write your own from scratch, using whatever computer language you prefer.

    1.- Write a program to calculate and print out the histogram
    of the number of times each side occurs, the deviation of this number from onesixth of the number of trials, the frequency with which each side occurs, and the
    deviation of this from one sixth. Hand in a copy of the code you used.
    2.- Show a typical print-out of your program.
    3.- Run the program for various numbers of random integers, starting with a small
    number, say 10, and increasing to a substantially larger number. The only upper
    limit is that the program should not take more than about one second to run. (Your
    time is valuable.)
    4.- As the number of trials increases, does the magnitude (absolute value) of the
    differences between the number of times a given side occurs and one-sixth of the
    number of trials increase or decrease?
    5.- As you increase the number of trials, does the ratio of the number of times each side
    occurs to the total number of trials come closer to 1/6?
"""

from die import Die
from clock import now

t0 = now()

#Here we create a list of 6-sided dice with an increasing number of trials
dice = [Die(10**i, 6) for i in range(1,7)]

for die in dice:
    die.throw()
    die.print_results()
    print("\n")

t1 = now()
print(f"Program time: {t1 - t0}")