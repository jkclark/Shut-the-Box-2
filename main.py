from box_state import BoxState
from data_visualization import show_all_visualizations
from dice import Dice
from game import Game
from strategy import ScoreOptimalStrategy, WinPercentHighestNumberStrategy, WinPercentMostNumbersHighStrategy, WinPercentMostNumbersLowStrategy, WinPercentOptimalStrategy


def main():
    # Set up
    MAX_NUMBER_IN_BOX = 12
    # starting_game_state.numbers MUST be a list of consecutive positive integers
    # starting with 1
    starting_game_state = BoxState([num for num in range(1, MAX_NUMBER_IN_BOX + 1)])
    dice = Dice([6, 6])
    strategies = [
        WinPercentOptimalStrategy(),
        # WinPercentMostNumbersHighStrategy(),
        # WinPercentMostNumbersLowStrategy(),
        # WinPercentHighestNumberStrategy(),
    ]

    for strategy in strategies:
        game = Game(
            starting_game_state,
            dice,
            strategy
        )

        game.solve_all_box_states()
        print(f"{strategy}: {game.all_box_states[starting_game_state.id].expectation}")

    # show_all_visualizations(game)
    print("")

if __name__ == "__main__":
    main()
