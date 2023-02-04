# ---------------------------- PROBLEM 3.3 STATEMENT ------------------------------- #
"""
A DIE WITH AN ARBITRARY NUMBER OF SIDES
Suppose we have a die with S sides, where S is an integer, but not necessarily equal
to 6. The set of possible outcomes is then {n|n = 1,...,S} (or {n|n = 0,...,S − 1}, your
choice). Assume that all sides of the die are equally probable, so that P(n) = 1/S.
Since this is partly a computational problem, be sure to support your answers with
data from your computer simulations.
    1. What are the theoretical values of the mean, variance, and standard deviation as
    functions of S? The answers should be in closed form, rather than expressed as a
    sum. (Hint: It might be helpful to review the formulas for the sums of integers and
    squares of integers.)
    2. Modify the program you used for an earlier problem to simulate rolling a die with
    S sides, and print out the mean, variance, and standard deviation for a number of
    trials. Have the program print out the theoretical predictions in each case, as well as
    the deviations from theory to facilitate comparisons.
    3. Run your program for two very different values of S. Are the results for the mean,
    variance, and standard deviation consistent with your predictions?
    (Do not use such long runs that the program takes more than about a second to run.
    It would be a waste of your time to wait for the program to finish.)
    4. Experiment with different numbers of trials. How many trials do you need to obtain
    a rough estimate for the values of the mean and standard deviation? How many trials
    do you need to obtain an error of less than 1%? Do you need the same number of
    trials to obtain 1% accuracy for the mean and standard deviation?
"""


from die import Die
sides = 16

dice = [Die(sides, int((10**exp)/2)) for exp in range(1,6)]

for die in dice:
    die.roll()
    die.print_results()