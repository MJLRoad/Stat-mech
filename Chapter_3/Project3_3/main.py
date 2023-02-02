from dice import Dice
sides = 69

dices = [Dice(sides, int((10**exp)/2)) for exp in range(1,6)]

for dice in dices:
    dice.roll()
    dice.print_results()
