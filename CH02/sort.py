"""
Lab 2: Sorting Algorithms
Implements selection sort with performance tracking.
"""
from typing import List, Dict, Callable


def find_smallest_index(arr: List[Dict], key: Callable, start: int) -> int:
    """
    Find index of smallest element from start position.
    
    Args:
        arr: List to search
        key: Function to extract comparison value
        start: Starting index
    
    Returns:
        Index of smallest element
    """
    # TODO: Implement find_smallest_index
    # 1. Initialize smallest_idx to start
    smallest_idx = start

    # 2. Get smallest_val using key(arr[start])
    smallest_val = key(arr[start])
    # 3. Loop from start+1 to end of array
    for i in range(start + 1, len(arr)):
        # 4. If key(arr[i]) < smallest_val, update smallest_val and smallest_idx
        if (key(arr[i]) < smallest_val):
            smallest_val = key(arr[i])
            smallest_idx = i 
    # 5. Return smallest_idx
    return smallest_idx
    


def selection_sort(arr: List[Dict], key: Callable = lambda x: x, reverse: bool = False) -> List[Dict]:
    """
    Sort list using selection sort algorithm.
    Time Complexity: O(n²)
    Space Complexity: O(n) - creates copy
    
    Args:
        arr: List to sort
        key: Function to extract comparison value
        reverse: If True, sort descending
    
    Returns:
        Sorted list (does not modify original)
    """
    # TODO: Implement selection_sort
    # 1. Get n = len(arr)
    n = len(arr) 
    # 2. Initialize comparisons = 0, swaps = 0
    comparisons = 0 
    swaps = 0
    # 3. Create result = arr.copy() to avoid modifying original
    result = arr.copy()
    
    # 4. Loop i from 0 to n-1:
    for i in range(n):
        extreme_idx = i

        #    a. If reverse, find largest element from i to end
        #    b. Else find smallest element from i to end
        for j in range(i + 1, n):
            comparisons += 1
            if reverse:
                if key(result[j]) > key(result[extreme_idx]):
                    extreme_idx = j
            else:
                if key(result[j]) < key(result[extreme_idx]):
                    extreme_idx = j

        #    c. Swap result[i] with result[extreme_idx] if needed
        if extreme_idx != i:
            result[i], result[extreme_idx] = result[extreme_idx], result[i]
            swaps += 1
    # 5. Print comparison and swap counts
    print(f"Selection Sort: comparisons={comparisons}, swaps={swaps}")

    # 6. Return result
    return result


def python_builtin_sort(arr: List[Dict], key: Callable, reverse: bool = False) -> List[Dict]:
    """
    Python's built-in sort for comparison.
    Time Complexity: O(n log n) - Timsort algorithm
    """
    # TODO: Implement python_builtin_sort
    # 1. Create result = arr.copy()
    result = arr.copy()
    # 2. Call result.sort(key=key, reverse=reverse)
    result.sort(key=key, reverse=reverse)
    # 3. Print "Python Built-in Sort: O(n log n) - Timsort"
    print ("Python Built-in Sort: O(n log n) - Timsort")
    # 4. Return result
    return result
