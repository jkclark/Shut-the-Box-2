from game import Game


def analyze(game: Game):
    starting_box_state_id = game.get_starting_box_state_id()
    print(f"{game.strategy} expectation: {game.all_box_states[starting_box_state_id].expectation}")
