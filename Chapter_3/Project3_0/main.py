from dice import Dice
from clock import now

t0 = now()

dice = Dice(10000, 6)
print(f"Number of trials: {dice.trials}")
dice.throw()
dice.print_results()

t1 = now()
print(f"Program time: {t1 - t0}")