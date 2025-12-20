# Shut the Box

## TODO:
- It is clear that we want to remove the fewest numbers possible, but which numbers should they be?
- How do things change if our goal is lowest score, not win% ?
- What is the difference in expectation between various strategies? Like, how much expectation do you lose
if you play with a suboptimal strategy?

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

Actually, the guiding principle is more general than that: in all but **8** situations (out of 45,045), we choose to remove the *fewest* number of numbers.
This moves us forward in the game while leaving us the most flexibility to deal with future rolls.

Here are the 8 situations:
- Chosen vs not chosen
- [4, 7]     vs [1, 2, 8] -- gain of 0.0062 expectation
- [4, 8]     vs [1, 2, 9] -- gain of 0.0062 expectation
- [5, 6]     vs [1, 2, 8] -- gain of 0.0093 expectation
- [5, 7]     vs [1, 2, 9] -- gain of 0.0201 expectation
- [5, 7]     vs [1, 3, 8] -- gain of 0.0015 expectation
- [1, 8, 11] vs [2, 3, 4, 11] -- gain of 0.0003 expectation
- [4, 7, 12] vs [1, 2, 8, 12] -- gain of 0.0005 expectation
- [5, 6, 12] vs [1, 2, 8, 12] -- gain of 0.0008 expectation

As you can see, in these exceptional cases, we would be stuck with numbers on the extreme ends
of the spectrum, and instead we choose to have fewer numbers to close, but which are more likely
to be rolled.

In the other 45,037 situations, we choose to remove the fewest number of numbers (although which set of that number of numbers is not necessarily clear yet). That is to say,
it is correct to remove the fewest number of numbers in ~99.982% of game states.
