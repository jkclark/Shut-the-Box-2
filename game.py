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
        self.max_box_number = len(starting_box_state.numbers)
        self.dice = dice
        self.strategy = strategy

        # Establish shut-box value
        closed_box_state = BoxState([])
        closed_box_state.expectation = self.strategy.get_game_over_box_state_value(closed_box_state)

        # Set up box-state data structure
        self.all_box_states = {}
        self.all_box_states[closed_box_state.id] = closed_box_state

    def solve(self) -> None:
        self.solve_all_box_states()
        self.get_all_box_state_probabilities()

    def solve_all_box_states(self) -> None:
        for num_of_nums_in_box in range(1, self.max_box_number + 1):
            for combo in combinations(range(1, self.max_box_number + 1), num_of_nums_in_box):
                box_state = BoxState(list(combo))
                self.solve_box_state(box_state)
                self.all_box_states[box_state.id] = box_state

    def solve_box_state(self, box_state: BoxState):
        # Check memo
        if box_state.expectation is not None:
            return box_state.expectation

        box_value = 0
        for dice_sum, prob in self.dice.distribution.items():
            # What are the possible box states (by ID) we can get to from here?
            possible_next_box_state_ids = self.get_ids_of_next_box_state_options_given_roll(box_state, dice_sum)

            # If there are no possible next box states, consider this state as game over
            if len(possible_next_box_state_ids) == 0:
                # Get the value of this state being game over
                next_game_state_expectation = self.strategy.get_game_over_box_state_value(box_state)

                # Remember that for the current box state, this roll yields game over
                box_state.rolls_to_next_box_states[dice_sum] = None

            # Choose the next box state according to the strategy
            else:
                # Get the actual BoxState objects for the candidates
                possible_next_box_states = [
                    self.all_box_states[possible_next_box_state_id]
                    for possible_next_box_state_id in possible_next_box_state_ids
                ]

                # Choose the next box state
                chosen_next_box_state = self.strategy.pick_next_box_state_from_options(possible_next_box_states)

                # Remember that we chose this one for the current box state
                box_state.rolls_to_next_box_states[dice_sum] = chosen_next_box_state

                # Get the expectation of the next state
                next_game_state_expectation = chosen_next_box_state.expectation

            # Multiply the value by the probability
            next_box_state_weighted_value = next_game_state_expectation * prob

            # Add that value to box_value
            box_value += next_box_state_weighted_value

        box_state.expectation = box_value

    def get_ids_of_next_box_state_options_given_roll(self, box_state: BoxState, roll: int) -> Set[str]:
        # If there is still roll to use and we have no numbers left, we've lost (not a valid box state)
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

    def get_all_box_state_probabilities(self):
        # Set initial box state probability to 1
        initial_box_state = self.all_box_states[self.get_starting_box_state_id()]
        initial_box_state.probability = 1

        # Iterate through all combinations of progressively "more closed" boxes
        # and add their probabilities to their children
        for num_of_nums_in_box in range(self.max_box_number, 0, -1):
            for combo in combinations(range(1, self.max_box_number + 1), num_of_nums_in_box):
                box_state = self.all_box_states[BoxState.get_id(combo)]
                for dice_sum, next_box_state in box_state.rolls_to_next_box_states.items():
                    if next_box_state is not None:
                        next_state_prob = self.dice.distribution[dice_sum]
                        next_box_state.probability += box_state.probability * next_state_prob

    def get_starting_box_state_id(self) -> str:
        return ",".join([str(num) for num in range(1, self.max_box_number + 1)])
