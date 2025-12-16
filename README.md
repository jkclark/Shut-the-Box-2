# Shut the Box

## Rules

- When the box is fully "open": numbers 1-12
- Try to "close" each number
- Box is "shut" when no numbers remain

## Findings

- Board states: 2<sup>12</sup> = 4,096
- Distinct sums of 2 6-sided dice: 6 + 6 - 1 = 11 (e.g., 2, 3, 4, ..., 10, 11, 12)
- Distinct game states: 4,096 x 11 = 45,056
- Distinct game states with shut-box state removed: (4096 - 1) x 11 = 45,045

45,045 states where you roll the dice and you have to make a decision (or realize the game is over) -- this includes the box with only `1` still open, where you have definitely lost even before you roll.

### What number(s) to close?

- When possible, what % of the time is it optimal to close the number you just rolled? Based on initial inspection it seems quite high.
- When possible, what % of the time is it optimal NOT to?
- Is there a way to tell? Is there some feature that the do's/do not's have in common?
- How often will it not be possible?
