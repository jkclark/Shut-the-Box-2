from abc import ABC, abstractmethod
from typing import Set

from box_state import BoxState


class Strategy(ABC):
    """A strategy is responsible for evaluating a game-over state's value and for picking the next game state.
    
    These are relatively disconnected responsibilities, but for this relatively simple project I think
    it's fine to lump these together into one "Strategy" class.
    """
    @staticmethod
    @abstractmethod
    def get_game_over_box_state_value(box_state: BoxState) -> int:
        """Determine the value of the given box state if the game is over."""
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def pick_next_box_state_from_options(box_states: list[BoxState]) -> BoxState:
        """Pick the next game state from the given options."""
        raise NotImplementedError


class WinPercentStrategy(Strategy):
    @staticmethod
    def get_game_over_box_state_value(box_state: BoxState):
        return 1 if len(box_state.numbers) == 0 else 0

class WinPercentOptimalStrategy(WinPercentStrategy):
    def __str__(self):
        return "\"Win % - Optimal\" strategy"

    @staticmethod
    def pick_next_box_state_from_options(box_states: list[BoxState]) -> BoxState:
        # NOTE: This strategy does not discriminate between tied box states
        # This can lead to different outcomes in different runs of the script.
        best_option = None
        for box_state in box_states:
            if not best_option or box_state.expectation > best_option.expectation:
                best_option = box_state
        return best_option

class WinPercentOptimalThenFewestStrategy(WinPercentStrategy):
    """
    In digging into the optimal strategy, it was clear that most of the time, it's more optimal
    to remove the number = sum of the dice. There were some situations where the next box state
    where the dice-sum number was removed was tied with another option. This strategy eliminates
    those ties by taking the next box state with the most remaining numbers (thus the fewest removed),
    which will always be the option with the dice-sum number, if present.
    """
    def __str__(self):
        return "\"Win % - Optimal, then fewest numbers\" strategy"

    @staticmethod
    def pick_next_box_state_from_options(box_states: list[BoxState]) -> BoxState:
        sorted_next_box_states_optimal_then_fewest = sorted(
            box_states,
            key=lambda state: (state.expectation, len(state.numbers)),
            reverse=True,
        )

        return sorted_next_box_states_optimal_then_fewest[0]


class WinPercentMostNumbersHighStrategy(WinPercentStrategy):
    def __str__(self):
        return "\"Win % - most numbers, then high\" strategy"

    @staticmethod
    def pick_next_box_state_from_options(box_states: list[BoxState]) -> BoxState:
        """Pick the state that removes the most numbers, or the one that removes the highest number if tied."""
        sorted_by_num_of_nums = sorted(
            box_states,
            key=lambda state: (len(state.numbers), max(state.numbers) if len(state.numbers) > 0 else 0)
        )
        return sorted_by_num_of_nums[0]


class WinPercentMostNumbersLowStrategy(WinPercentStrategy):
    def __str__(self):
        return "\"Win % - most numbers, then low\" strategy"

    @staticmethod
    def pick_next_box_state_from_options(box_states: list[BoxState]) -> BoxState:
        """Pick the state that removes the most numbers, or the one that removes the lowest number if tied."""
        sorted_by_num_of_nums = sorted(
            box_states,
            # When tied, we want to pick the box state that removed the lowest number
            # The box state that removed the lowest number will have a higher min
            # Since we sort in ASC order, we negate each min to put them in the right order.
            key=lambda state: (len(state.numbers), -1 * min(state.numbers) if len(state.numbers) > 0 else 0)
        )
        return sorted_by_num_of_nums[0]


class WinPercentHighestNumberStrategy(WinPercentStrategy):
    def __str__(self):
        return "\"Win % - highest number first\" strategy"

    @staticmethod
    def pick_next_box_state_from_options(box_states: list[BoxState]) -> BoxState:
        """Pick the state that removes the highest number (next highest number if tied)."""
        sorted_by_num_of_nums = sorted(
            box_states,
            key=lambda state: tuple(sorted(state.numbers, reverse=True))
        )
        return sorted_by_num_of_nums[-1]  # There should always be at least 1


class ScoreStrategy(Strategy):
    @staticmethod
    def get_game_over_box_state_value(box_state: BoxState) -> int:
        return sum(box_state.numbers)


class ScoreOptimalStrategy(ScoreStrategy):
    def __str__(self):
        return "Strategy: score: optimal"

    @staticmethod
    def pick_next_box_state_from_options(box_states: list[BoxState]) -> BoxState:
        best_option = None
        for box_state in box_states:
            if not best_option or box_state.expectation < best_option.expectation:
                best_option = box_state
        return best_option
