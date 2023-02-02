from dice import Dice
from clock import now

t0 = now()

dices = [Dice(10**i, 6) for i in range(1,7)]
for dice in dices:
    dice.throw()
    dice.print_results()
    print("\n")

t1 = now()
print(f"Program time: {t1 - t0}")