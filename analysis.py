from game import Game


def analyze(solved_game: Game):
    starting_box_state_id = solved_game.get_starting_box_state_id()
    print(f"{solved_game.strategy} expectation: {solved_game.all_box_states[starting_box_state_id].expectation}")

    get_numbers_to_close_stats(solved_game)

def get_numbers_to_close_stats(game: Game) -> None:
    game_states_to_counts = {
        "total": 0,
        "game_over": 0,
        "can_close_dice_roll": 0,
        "cannot_close_dice_roll": 0,
        "can_and_should_close_dice_roll": 0,
        "can_and_should_not_close_dice_roll": 0,
    }

    for box_state in game.all_box_states.values():
        for dice_roll, next_box_state in box_state.rolls_to_next_box_states.items():
            if next_box_state is None:
                game_over_prob = box_state.probability * game.dice.distribution[dice_roll]
                game_states_to_counts["game_over"] += 1
                game_states_to_counts["total"] += 1
                continue

            if dice_roll in box_state.numbers:
                game_states_to_counts["can_close_dice_roll"] += 1
                game_states_to_counts["total"] += 1

                if dice_roll not in next_box_state.numbers:
                    game_states_to_counts["can_and_should_close_dice_roll"] += 1
                else:
                    game_states_to_counts["can_and_should_not_close_dice_roll"] += 1

            else:
                game_states_to_counts["cannot_close_dice_roll"] += 1
                game_states_to_counts["total"] += 1

                # Print out situation
                numbers_removed = len(box_state.numbers) - len(next_box_state.numbers)
                print(f"{box_state.numbers} & {dice_roll} -> {numbers_removed}")

    for situation, count in game_states_to_counts.items():
        print(f"{situation}: {count}")
