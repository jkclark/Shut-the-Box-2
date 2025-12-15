from itertools import combinations
from typing import Callable, Set

from box_state import BoxState
from dice import Dice
from strategy import Strategy


class Game():
    def __init__(
        self,
        starting_box_state: BoxState,
        dice: Dice,
        strategy: Strategy,
    ) -> None:
        # NOTE: starting_box_state.numbers MUST be a list of consecutive
        #       positive integers starting at 1
        self.starting_box_state = starting_box_state
        self.dice = dice
        self.strategy = strategy

        # Establish shut-box value
        closed_box_state = BoxState([])
        closed_box_state.expectation = self.strategy.get_game_over_box_state_value(closed_box_state)

        # Set up box-state data structure
        self.all_box_states = {}
        self.all_box_states[closed_box_state.id] = closed_box_state

    def solve_all_box_states(self) -> None:
        max_num_of_nums = len(self.starting_box_state.numbers)
        for num_of_nums_in_box in range(1, max_num_of_nums + 1):
            for combo in combinations(range(1, max_num_of_nums + 1), num_of_nums_in_box):
                box_state = BoxState(list(combo))
                self.solve_box_state(box_state)
                self.all_box_states[box_state.id] = box_state

    def solve_box_state(self, box_state: BoxState):
        # Check memo
        if box_state.expectation is not None:
            return box_state.expectation

        box_value = 0
        for dice_sum, prob in self.dice.distribution.items():
            # What are the possible box states we can get to from here?
            possible_next_box_state_ids = self.get_ids_of_next_box_state_options_given_roll(box_state, dice_sum)

            # If there are no possible next game states, consider this state as game over
            if len(possible_next_box_state_ids) == 0:
                next_game_state_expectation = self.strategy.get_game_over_box_state_value(box_state)

            # Choose the next box state according to the strategy
            else:
                possible_next_box_states = [
                    self.all_box_states[possible_next_box_state_id]
                    for possible_next_box_state_id in possible_next_box_state_ids
                ]
                chosen_next_game_state = self.strategy.pick_next_box_state_from_options(possible_next_box_states)
                next_game_state_expectation = chosen_next_game_state.expectation

            # Multiply the value by the probability
            next_box_state_weighted_value = next_game_state_expectation* prob

            # Add that value to box_value
            box_value += next_box_state_weighted_value

        box_state.expectation = box_value

    def get_ids_of_next_box_state_options_given_roll(self, box_state: BoxState, roll: int) -> Set[str]:
        # If there is still roll to use and we have no numbers left, we've lost (not a valid game state)
        if roll > 0 and len(box_state.numbers) == 0:
            return set()

        # If the roll is 0, we've won
        if roll == 0:
            return {box_state.id}

        # Iterate over each number in the box, removing it and trying again that much less roll
        next_box_state_option_ids = set()
        for number in box_state.numbers:
            if number > roll:
                return next_box_state_option_ids

            # Get the box state when we remove this number
            next_box_state_numbers = [*box_state.numbers]
            next_box_state_numbers.remove(number)
            next_box_state = BoxState(next_box_state_numbers)

            # Recursive step
            all_next_box_states_minus_number = self.get_ids_of_next_box_state_options_given_roll(next_box_state, roll - number)

            # Add all those states to the set
            next_box_state_option_ids = next_box_state_option_ids | all_next_box_states_minus_number

        return next_box_state_option_ids
