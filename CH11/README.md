[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=23853013&assignment_repo_type=AssignmentRepo)
# Knapsack Problem - Dynamic Programming

## Overview

In this assignment, you'll implement the classic **knapsack problem** using dynamic programming. The knapsack problem is a fundamental optimization problem where you have a knapsack with limited weight capacity and a collection of items, each with a weight and value. Your goal is to select items that maximize the total value while staying within the weight limit.

This is a perfect introduction to dynamic programming - a powerful technique that solves complex problems by breaking them down into simpler subproblems and storing their solutions to avoid redundant calculations.

## Learning Objectives

By completing this assignment, you will:
- Understand the core concepts of dynamic programming
- Learn how to identify and solve optimization problems using DP
- Practice building and filling 2D tables to store subproblem solutions
- Develop problem-solving skills for breaking down complex problems

## Getting Started

1. Accept the GitHub Classroom assignment
2. Clone your repository to your local machine
3. Open `main.py` in your preferred Python editor
4. Read through the starter code to understand the structure
5. Complete the TODOs step by step

## Understanding the Problem

The knapsack problem works like this:
- You have a knapsack that can hold a maximum weight
- You have several items, each with a name, weight, and value
- You want to pack items to maximize total value without exceeding weight capacity

**Dynamic Programming Approach:**
We'll create a 2D grid where `grid[i][w]` represents the optimal solution using the first `i` items with weight capacity `w`. Each cell will store a list of items that gives the maximum value for that subproblem.

## Requirements

Complete the following TODOs in order:

### 1. Fill the Dynamic Programming Grid (`knapsack` function)

For each item and each possible capacity:

**TODO 1:** Check if the current item's weight exceeds the current capacity
- If `weight > w`, the item won't fit

**TODO 2:** If item is too heavy, copy the solution from the previous row
- Use `grid[i-1][w]` (same capacity, but without considering current item)

**TODO 3:** Calculate the value if we include the current item
- Find the best solution with remaining capacity: `grid[i-1][w-weight]`
- Add the current item to that solution

**TODO 4:** Get the value if we exclude the current item
- This is simply `grid[i-1][w]`

**TODO 5:** Choose the better option
- Calculate total values for both include/exclude options
- Store the solution with higher total value in `grid[i][w]`

**Hint:** To calculate total value of a solution, sum up all item values in the list.

### 2. Display the Grid (`display_grid` function)

**TODO 6:** Print header row with capacity numbers
- Format: spaces followed by capacity numbers (1, 2, 3, etc.)

**TODO 7:** Start each row with the item name
- Use the item name from the items list

**TODO 8:** Format each cell to show items and total value
- Format: `$value(items)` where items are first letters
- Example: `$4500(GS)` means total value $4500 with Guitar and Stereo

**TODO 9:** Add empty spaces for cells with no items

### 3. Main Execution

**TODO 10:** Call the knapsack function with the provided items and capacity

**TODO 11:** Uncomment and call the display_grid function

## Example Input/Output

**Input:**
```python
items = [
    ("GUITAR", 1, 1500),
    ("STEREO", 4, 3000),
    ("LAPTOP", 3, 2000),
    ("iPHONE", 1, 2000),
    ("BOOK", 2, 100),
    ("GOLD BAR", 1, 30000)
]
capacity = 6
```

**Expected Output:**
```
            1           2           3           4           5           6
GUITAR      $1500(G)    $1500(G)    $1500(G)    $1500(G)    $1500(G)    $1500(G)
STEREO      $1500(G)    $1500(G)    $1500(G)    $3000(S)    $4500(GS)   $4500(GS)
LAPTOP      $1500(G)    $1500(G)    $2000(L)    $3500(GL)   $4500(GS)   $5500(GLS)
iPHONE      $2000(I)    $3500(GI)   $3500(GL)   $4000(LI)   $5500(GLI)  $6500(GLSI)
BOOK        $2000(I)    $3500(GI)   $3600(GIB)  $4000(LI)   $5500(GLI)  $6500(GLSI)
GOLD BAR    $30000(G)   $31500(GG)  $32000(GI)  $33500(GGI) $33600(GGIB)$35500(GGLI)
```

## Helpful Hints

1. **Start small:** Test with just the first 2-3 items to understand the pattern
2. **Think recursively:** For each item, you either include it or you don't
3. **Check your logic:** The value should never decrease as you move right or down in the grid
4. **Debug step by step:** Print intermediate values to understand what's happening
5. **Remember:** `grid[i][w]` stores a LIST of items, not just the total value

## Testing Your Solution

Run your program with:
```bash
python main.py
```

The autograder will test your solution with various inputs to ensure correctness.

## Submission Instructions

1. Complete all TODOs in `main.py`
2. Test your solution locally to ensure it works
3. Commit your changes:
   ```bash
   git add main.py
   git commit -m "Complete knapsack dynamic programming solution"
   ```
4. Push to trigger the autograder:
   ```bash
   git push origin main
   ```

The autograder will run automatically and provide feedback on your solution. Make sure all tests pass before considering the assignment complete!