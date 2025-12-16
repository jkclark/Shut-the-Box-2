from box_state import BoxState
from data_visualization import show_all_visualizations
from dice import Dice
from game import Game
from strategy import WinPercentMostNumbersHighStrategy, WinPercentOptimalStrategy


def main():
    # Set up
    MAX_NUMBER_IN_BOX = 12
    # starting_game_state.numbers MUST be a list of consecutive positive integers
    # starting with 1
    starting_game_state = BoxState([num for num in range(1, MAX_NUMBER_IN_BOX + 1)])
    dice = Dice([6, 6])
    strategy = WinPercentOptimalStrategy()
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
    show_all_visualizations(game)

if __name__ == "__main__":
    main()
