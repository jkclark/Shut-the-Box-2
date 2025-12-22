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

Actually, the guiding principle is more general than that: in all but **8** situations (out of 45,045), we choose to remove the _fewest_ number of numbers.
This moves us forward in the game while leaving us the most flexibility to deal with future rolls.

Here are the 8 situations:
| Box State | Roll | Chosen | Not Chosen | Expectation gain |
|-----------|------|--------|------------|------------------|
|1,2,4,7,8|11|4,7|1,2,8|0.0062|
|1,2,4,8,9|12|4,8|1,2,9|0.0062|
|1,2,5,6,8|11|5,6|1,2,8|0.0093|
|1,2,5,7,9|12|5,7|1,2,9|0.0201|
|1,3,5,7,8|12|5,7|1,3,8|0.0015|
|1,2,3,4,8,11|9|1,8,11|2,3,4,11|0.0003|
|1,2,4,7,8,12|11|4,7,12|1,2,8,12|0.0005|
|1,2,5,6,8,12|11|5,6,12|1,2,8,12|0.0008|

If we take difference between the expectation of the best option and the expectation of
the next best option that removes _more_ numbers, we get an average of 0.0165248 across
27,542 situations where there is such a next best option.

As you can see, in these exceptional cases, we would be stuck with numbers on the extreme ends
of the spectrum, and instead we choose to have fewer numbers to close, but which are more likely to be rolled.

In the other 45,037 situations, we choose to remove the fewest number of numbers (although which set of that number of numbers is not necessarily clear yet). That is to say,
it is correct to remove the fewest number of numbers in ~99.982% of game states.
