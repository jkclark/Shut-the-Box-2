from box_state import BoxState
from dice import Dice
from game import Game
from strategy import WinPercentMostNumbersHighStrategy, WinPercentOptimalStrategy


def main():
    # Set up
    starting_game_state = BoxState([num for num in range(1, 13)])
    dice = Dice([6, 6])
    # strategy = WinPercentOptimalStrategy()
    strategy = WinPercentMostNumbersHighStrategy()
    print(dice.distribution)
    game = Game(
        starting_game_state,
        dice,
        strategy
    )

    # Play
    game.solve_all_box_states()

    # Print
    print("Strategy:", str(strategy))
    print("Expectation with above strategy:", game.all_box_states[starting_game_state.id].expectation)

if __name__ == "__main__":
    main()
