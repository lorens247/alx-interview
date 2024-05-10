#   0x03 -  Island Perimeter

## Description

This Python script calculates the perimeter of an island represented by a 2D grid.

## Problem Statement

Given a 2D grid `grid` where each cell is either 0 (water) or 1 (land), calculate the perimeter of the island. The island is surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

## Concepts

### 2D Arrays (Matrices)

- Accessing and iterating over elements in a 2D array.
- Navigating through adjacent cells (horizontally and vertically).

### Conditional Logic

- Applying conditions to determine whether a cell contributes to the perimeter of the island.

### Counting Techniques

- Developing a method to count the edges that contribute to the island’s perimeter.

### Problem-Solving Strategies

- Breaking down the problem into smaller tasks, such as identifying land cells and calculating their contribution to the perimeter.

### Python Programming

- Using nested loops for iterating over grid cells.
- Utilizing conditional statements to check the status of adjacent cells.

## Usage

1. Ensure you have Python installed on your machine.
2. Clone the repository or download the `island_perimeter.py` file.
3. Run the script by executing `python island_perimeter.py`.
4. Follow the on-screen instructions to input the 2D grid representing the island.
5. The script will output the perimeter of the island.

## Example

```python
Input:
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
Output:
16
```
