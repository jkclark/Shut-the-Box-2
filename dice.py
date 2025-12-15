from decimal import Decimal
import random


class Dice():
    def __init__(self, dice_num_sides: list[int]) -> None:
        self.sides = dice_num_sides
        self.distribution = self.get_distribution()
    
    def get_distribution(self) -> dict[int, Decimal]:
        dist = {0: Decimal(1)}  # Start with no dice
        for s in self.sides:
            new_dist = {}
            for current_sum, prob in dist.items():
                for face in range(1, s + 1):
                    new_sum = current_sum + face
                    new_dist[new_sum] = new_dist.get(new_sum, Decimal(0)) + prob / Decimal(s)
            dist = new_dist
        return dist
