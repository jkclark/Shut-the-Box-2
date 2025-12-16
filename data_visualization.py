import matplotlib.pyplot as plt

from game import Game

def show_all_visualizations(solved_game: Game) -> None:
    show_avg_expectation_by_num_of_remaining_nums(solved_game)

def show_avg_expectation_by_num_of_remaining_nums(solved_game: Game) -> None:
    # number of numbers in box (n) --> [sum of expectations, number of box states with n numbers]
    avg_expectation_data_by_num_of_nums_left = {}
    
    for box_state in solved_game.all_box_states.values():
        num_of_nums = len(box_state.numbers)

        # Increment the values
        try:
            avg_expectation_data = avg_expectation_data_by_num_of_nums_left[num_of_nums]
            avg_expectation_data[0] += box_state.expectation
            avg_expectation_data[1] += 1

        # Create a new entry and set the values for the first time
        except KeyError:
            avg_expectation_data_by_num_of_nums_left[num_of_nums] = [
                box_state.expectation,
                1
            ]

    # Calculate the averages per number
    avg_expectations = []
    for num_of_nums, avg_data in avg_expectation_data_by_num_of_nums_left.items():
        avg_expectations.append((num_of_nums, avg_data[0] / avg_data[1]))

    nums, avgs = zip(*avg_expectations)

    plt.bar(nums, avgs)
    plt.xlabel("Number of numbers remaining")
    plt.ylabel("Average expectation")
    plt.title("Average expectation by number of remaining numbers")
    plt.show()
