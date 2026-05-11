# Chapter 1 Lab: Binary Search vs Linear Search

## Overview

Starting from a basic program structure with timing functions and test data, students will implement both linear search and binary search algorithms to demonstrate the performance differences between these fundamental search techniques. This lab provides hands-on experience with algorithm efficiency and Big O notation concepts.

## Learning Objectives

- Demonstrate binary search vs. linear search
- Implement linear search algorithm
- Implement binary search algorithm following provided pseudocode
- Compare timing performance between search algorithms
- Calculate theoretical maximum steps for binary search

## Requirements

1. Complete the `linear_search()` function body that searches through an array sequentially
2. Complete the `binary_search()` function body that searches through a sorted array using the divide-and-conquer approach
3. Ensure both functions return the correct index when an item is found, or `None` when not found
4. The program must execute without errors and produce timing comparisons
5. Answer the lab challenge question about maximum steps for binary search in 128 items

## Getting Started

The starter code provides a complete testing framework with timing functions and test data. It includes:
- Empty function stubs for `linear_search()` and `binary_search()`
- A `time_search_comparison()` function that measures execution time for both algorithms
- A main section that tests both algorithms with 10 different search values in a sorted list of 128 numbers
- Output formatting that displays timing results and performance comparisons

## Implementation Steps

### Implement Linear Search Algorithm

Complete the `linear_search()` function to search through an array element by element. The algorithm should check each position in order until it finds the target item or reaches the end of the array.

For example, when searching for `64` in `[1, 2, 3, ..., 128]`, linear search will check positions 0, 1, 2, ... until it reaches position 63 where it finds the value 64.

```python
def linear_search(arr, item):
    """
    Performs linear search on an array.
    Returns the index if found, None otherwise.
    """
    # Loop through each element in the array
    for i in range(len(arr)):
        # Compare each element with the target item
        if arr[i] == item:
            # Return the index when found
            return i
    # Return None if not found
    return None
```

### Implement Binary Search Algorithm

Complete the `binary_search()` function following the provided pseudocode. This algorithm works by repeatedly dividing the search space in half, comparing the middle element with the target, and eliminating half of the remaining elements.

For example, when searching for `64` in `[1, 2, 3, ..., 128]`:
- First check middle (position 64, value 65) - too high, search left half
- Check middle of left half (position 32, value 33) - too low, search right half of left half
- Continue until finding position 63 with value 64

```python
def binary_search(arr, item):
    """
    Performs binary search on a sorted array.
    Returns the index if found, None otherwise.
    """
    # Set low and high boundaries
    low = 0
    high = len(arr) - 1
    
    # Continue searching while the range is valid
    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2
        guess = arr[mid]
        
        # Check if we found the item
        if guess == item:
            return mid
        # If guess is too high, search the lower half
        elif guess > item:
            high = mid - 1
        # If guess is too low, search the upper half
        else:
            low = mid + 1
    
    # Return None if item not found
    return None
```

## Complete Program

```python
import time
import math

def linear_search(arr, item):
    """
    Performs linear search on an array.
    Returns the index if found, None otherwise.
    """
    # Loop through each element in the array
    for i in range(len(arr)):
        # Compare each element with the target item
        if arr[i] == item:
            # Return the index when found
            return i
    # Return None if not found
    return None

def binary_search(arr, item):
    """
    Performs binary search on a sorted array.
    Returns the index if found, None otherwise.
    """
    # Set low and high boundaries
    low = 0
    high = len(arr) - 1
    
    # Continue searching while the range is valid
    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2
        guess = arr[mid]
        
        # Check if we found the item
        if guess == item:
            return mid
        # If guess is too high, search the lower half
        elif guess > item:
            high = mid - 1
        # If guess is too low, search the upper half
        else:
            low = mid + 1
    
    # Return None if item not found
    return None

def time_search_comparison(arr, target):
    """
    Times both search algorithms and returns the results.
    Returns a tuple of (linear_time, binary_time, linear_result, binary_result)
    """
    # Time linear search
    start_time = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start_time
    
    # Time binary search
    start_time = time.time()
    binary_result = binary_search(arr, target)
    binary_time = time.time() - start_time
    
    return linear_time, binary_time, linear_result, binary_result

# Main execution with hardcoded data
if __name__ == "__main__":
    # Create a sorted list of 128 names (using numbers for simplicity)
    sorted_names = list(range(1, 129))  # [1, 2, 3, ..., 128]
    
    # Test cases - searching for different items
    test_items = [1, 64, 128, 50, 100, 25, 75, 10, 90, 200]  # 200 is not in the list
    
    print("Binary Search vs Linear Search Time Comparison")
    print("================================================")
    print("Searching in a sorted list of 128 numbers")
    print()
    
    for item in test_items:
        linear_time, binary_time, linear_result, binary_result = time_search_comparison(sorted_names, item)
        
        print(f"Searching for: {item}")
        print(f"Linear search time: {linear_time:.8f} seconds")
        print(f"Binary search time: {binary_time:.8f} seconds")
        print(f"Linear search result: {linear_result}")
        print(f"Binary search result: {binary_result}")
        
        if linear_time > 0 and binary_time > 0:
            speedup = linear_time / binary_time
            print(f"Binary search is {speedup:.2f}x faster")
        print()
    
    # Answer the lab challenge question
    print("Lab Challenge Answer:")
    print("Maximum steps for binary search in 128 items:")
    max_steps = math.ceil(math.log2(128))
    print(f"log2(128) = {max_steps} steps maximum")
```

## Testing

Commit and push your completed code to trigger the autograder. Check your repository on GitHub to see the test results. The autograder will verify that your program runs correctly and produces the expected output format with timing comparisons.

## Grading Rubric

| Test Name | Points |
|-----------|---------|
| Program executes without errors | 25 |
| Demonstrates binary search implementation | 20 |
| Demonstrates linear search implementation | 20 |
| Shows timing comparison between algorithms | 15 |
| Answers lab challenge about maximum steps | 10 |
| Calculates correct maximum steps using log2 | 10 |

## Tips and Hints

- Remember that binary search only works on sorted arrays - the test data is already sorted for you
- Use integer division (`//`) when calculating the middle index to avoid floating-point results
- The `time.time()` function returns seconds as a float - very small timing differences are normal
- For binary search, make sure to update `low` and `high` correctly: when the guess is too high, set `high = mid - 1`; when too low, set `low = mid + 1`
- The maximum steps for binary search is calculated using `math.ceil(math.log2(n))` where n is the array size
- Both search functions should return the index (integer) when found, or `None` when the item doesn't exist in the array

# Lab Report — [Lab Title]

## Student Information
- **Name:** Donghyun Lee
- **Date:** 2026-05-07
- **Course:** COSC 2436

---

## Algorithm Summary
[Plain-English explanation of how the algorithm or data structure works.]
Linear search checks every element one by one from the beginning until it finds the target. Binary search only works on sorted data and repeatedly cuts the search space in half by checking the middle element much faster for large lists.
- **Time Complexity (Big O):** [e.g., O(n log n) average, O(n²) worst] O(n) for linear and O(log n) for binary
- **Space Complexity:** [e.g., O(n)] O(1) for both
- **When to use it:** [Typical use cases / when this is the right tool] Linear search when searching in a small and unsorted list and binary search when searching in a sorted and large list. 

---

## Test Results
[Output, measurements, or results your program produced. Use the variant that fits this lab.]

### Search / Sort Labs
| Input Size |             Comparisons            |                      Time (ms)                    |
|------------|------------------------------------|---------------------------------------------------|
|     1      |   Linear search is 1.10x faster    |      0.00000238 seconds vs  0.00000262 seconds    | Linear vs Binary
|    128     |   Binary search is 2.17x faster    |      0.00000310 seconds vs  0.00000143 seconds    | Linear vs Binary


Binary Search vs Linear Search Time Comparison
================================================
Searching in a sorted list of 128 numbers

Searching for: 1
Linear search time: 0.00000238 seconds
Binary search time: 0.00000262 seconds
Linear search result: 0
Binary search result: 0
Binary search is 0.91x faster

Searching for: 64
Linear search time: 0.00000262 seconds
Binary search time: 0.00000072 seconds
Linear search result: 63
Binary search result: 63
Binary search is 3.67x faster

Searching for: 128
Linear search time: 0.00000310 seconds
Binary search time: 0.00000143 seconds
Linear search result: 127
Binary search result: 127
Binary search is 2.17x faster

Searching for: 50
Linear search time: 0.00000215 seconds
Binary search time: 0.00000119 seconds
Linear search result: 49
Binary search result: 49
Binary search is 1.80x faster

Searching for: 100
Linear search time: 0.00000310 seconds
Binary search time: 0.00000191 seconds
Linear search result: 99
Binary search result: 99
Binary search is 1.62x faster

Searching for: 25
Linear search time: 0.00000167 seconds
Binary search time: 0.00000191 seconds
Linear search result: 24
Binary search result: 24
Binary search is 0.88x faster

Searching for: 75
Linear search time: 0.00000167 seconds
Binary search time: 0.00000119 seconds
Linear search result: 74
Binary search result: 74
Binary search is 1.40x faster

Searching for: 10
Linear search time: 0.00000048 seconds
Binary search time: 0.00000072 seconds
Linear search result: 9
Binary search result: 9
Binary search is 0.67x faster

Searching for: 90
Linear search time: 0.00000215 seconds
Binary search time: 0.00000095 seconds
Linear search result: 89
Binary search result: 89
Binary search is 2.25x faster

Searching for: 200
Linear search time: 0.00000286 seconds
Binary search time: 0.00000095 seconds
Linear search result: None
Binary search result: None
Binary search is 3.00x faster

Lab Challenge Answer:
Maximum steps for binary search in 128 items:
log2(128) = 7 steps maximum


