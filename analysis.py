from game import Game


def analyze(game: Game):
    starting_box_state_id = game.get_starting_box_state_id()
    print(f"{game.strategy} expectation: {game.all_box_states[starting_box_state_id].expectation}")

    get_numbers_to_close_stats(game)

def get_numbers_to_close_stats(game: Game) -> None:
    situations_to_counts = {
        "game_over": 0,
        "can_close_dice_roll": 0,
        "cannot_close_dice_roll": 0,
        "can_and_should_close_dice_roll": 0,
        "can_and_should_not_close_dice_roll": 0,
    }

    for box_state in game.all_box_states.values():
        for dice_roll, next_box_state in box_state.rolls_to_next_box_states.items():
            if next_box_state is None:
                situations_to_counts["game_over"] += 1
                continue

            if dice_roll in box_state.numbers:
                situations_to_counts["can_close_dice_roll"] += 1

                if dice_roll not in next_box_state.numbers:
                    situations_to_counts["can_and_should_close_dice_roll"] += 1
                else:
                    situations_to_counts["can_and_should_not_close_dice_roll"] += 1
                    print(f"{box_state.numbers} & {dice_roll} --> {next_box_state.numbers}")

            else:
                situations_to_counts["cannot_close_dice_roll"] += 1

    for situation, count in situations_to_counts.items():
        print(f"{situation}: {count}")
