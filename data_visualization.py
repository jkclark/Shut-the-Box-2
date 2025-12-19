import matplotlib.pyplot as plt
import networkx as nx

from game import Game

def show_all_visualizations(solved_game: Game) -> None:
    # show_avg_expectation_by_num_of_remaining_nums(solved_game)
    show_game_graph(solved_game)

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

def show_game_graph(game: Game) -> None:
    visual = []

    def addEdge(a, b):
        temp = [a, b]
        visual.append(temp)

    def visualize():
        G = nx.Graph()
        G.add_edges_from(visual)

        # Arrange nodes: max length (7) at top (y=7), min length (0) at bottom (y=0)
        # Node id is a comma-separated string, e.g., "1,2,4"
        def node_len(node_id):
            if node_id == "":
                return 0
            return len(node_id.split(","))

        # Group nodes by their length
        nodes_by_len = {}
        for node in G.nodes:
            l = node_len(node)
            nodes_by_len.setdefault(l, []).append(node)

        pos = {}
        # For each length, arrange nodes horizontally, y = length
        for l in range(0, 8):  # 0 to 7
            nodes = nodes_by_len.get(l, [])
            for i, node in enumerate(nodes):
                pos[node] = (i, l)

        nx.draw_networkx(G, pos=pos)
        plt.show()

    for box_state_id, box_state in game.all_box_states.items():
        for dice_sum, next_game_state in box_state.rolls_to_next_box_states.items():
            if next_game_state is not None:
                addEdge(box_state_id, next_game_state.id)

    visualize()
