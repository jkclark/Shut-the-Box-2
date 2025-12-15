from box_state import BoxState
from dice import Dice
from game import Game
from strategy import WinPercentOptimalStrategy


def main():
    starting_game_state = BoxState([num for num in range(1, 10)])
    dice = Dice([6, 6])
    strategy = WinPercentOptimalStrategy
    print(dice.distribution)
    win_percent_game = Game(
        starting_game_state,
        dice,
        strategy
    )

    win_percent_game.solve_all_box_states()
    print("Done!")

if __name__ == "__main__":
    main()
