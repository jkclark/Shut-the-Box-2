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

Total game states: 45,045:

- game over: 10,845 (24.08%)
- can close dice roll: 22,528 (50.01%) (e.g., you roll an 8 and 8 is still open in the box)
- cannot close dice roll: (25.91%)

It turns out that it is always equal or better to close the sum of the dice if possible WHEN YOU ARE TRYING TO MAX WIN %

The above numbers equally weigh all game states, even though some are extremely unlikely to occur.
