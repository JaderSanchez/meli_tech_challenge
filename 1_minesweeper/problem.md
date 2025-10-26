# Problem

Transform a minesweeper board:

**Input:**

```
[
  [0, 1, 0, 0],
  [0, 0, 1, 0],
  [0, 1, 0, 1],
  [1, 1, 0, 0]
]
```

> 0 represents an empty space.

> 1 represents a mine.

**Output:**

```
[
  [1, 9, 2, 1],
  [2, 3, 9, 2],
  [3, 9, 4, 9],
  [9, 9, 3, 1]
]
```

Since in the output the numbers 0-8 are used to determine the amount of adjacent mines, the number 9 will be used to identify the mines instead.

## How I'll solve it:

1. First I'm going to change all 1 to 9 to represent mines and avoid to count false mines.

2. For each cell that is not a mine, I'm going to count the number of adjacent mines (including diagonals).

3. I'll update the cell with the count of adjacent mines.