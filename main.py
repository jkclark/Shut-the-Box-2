from analysis import analyze
from box_state import BoxState
from data_visualization import show_all_visualizations
from dice import Dice
from game import Game
from strategy import ScoreOptimalStrategy, WinPercentHighestNumberStrategy, WinPercentMostNumbersHighStrategy, WinPercentMostNumbersLowStrategy, WinPercentOptimalStrategy


def main():
    # Set up
    MAX_BOX_NUMBER = 12
    # NOTE: starting_box_state.numbers MUST be a list of consecutive
    #       positive integers starting at 1
    starting_game_state = BoxState([num for num in range(1, MAX_BOX_NUMBER + 1)])
    dice = Dice([6, 6])
    strategy = WinPercentOptimalStrategy()

    game = Game(
        starting_game_state,
        dice,
        strategy
    )
    game.solve_all_box_states()

    analyze(game)
    # show_all_visualizations(game)
    print("")

if __name__ == "__main__":
    main()
