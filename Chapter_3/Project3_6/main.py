from dice_manager import DiceManager

M = 2  #Number of sides on each dice
nb_trials = 10000

dice_managers = [DiceManager(N, M, nb_trials) for N in range(10, 110, 10)]

for dice_manager in dice_managers:
    print(f"We have {dice_manager.nb_dices} dices of {dice_manager.sides} sides each")
    print(f"Doing {dice_manager.trials} trials...")
    dice_manager.rolls()
    dice_manager.print_results()

