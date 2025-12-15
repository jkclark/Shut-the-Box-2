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
        pass

    @staticmethod
    @abstractmethod
    def pick_next_box_state_from_options(box_states: list[BoxState]) -> BoxState:
        """Pick the next game state from the given options."""
        pass


class WinPercentOptimalStrategy(Strategy):
    @staticmethod
    def get_game_over_box_state_value(box_state: BoxState) -> int:
        return 1 if len(box_state.numbers) == 0 else 0
    
    @staticmethod
    def pick_next_box_state_from_options(box_states: list[BoxState]) -> BoxState:
        best_option = None
        for box_state in box_states:
            if not best_option or box_state.expectation > best_option.expectation:
                best_option = box_state
        return best_option
