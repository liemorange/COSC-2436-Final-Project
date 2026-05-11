"""
Lab 03: Recursion
Implement recursive functions from Chapter 3.

Every recursive function has two cases:
1. Base case - when the function doesn't call itself
2. Recursive case - when the function calls itself
"""
from typing import List


def countdown(i: int) -> None:
    """
    Print countdown from i to 0.
    
    From Chapter 3 (page 45):
    Base case: i <= 0
    Recursive case: print i, then countdown(i-1)
    """
    # TODO: Implement countdown
    # 1. If i <= 0, print 0 and return
    if i <= 0:
        print (0)
        return
    # 2. Otherwise, print i
    else:
        print (i)
    # 3. Call countdown(i - 1)
        countdown(i-1)
    



def fact(x: int) -> int:
    """
    Calculate factorial of x recursively.
    
    From Chapter 3 (page 49):
    fact(5) = 5 * 4 * 3 * 2 * 1 = 120
    
    Base case: x == 1, return 1
    Recursive case: x * fact(x-1)
    """
    # TODO: Implement factorial
    # 1. If x <= 1, return 1 (base case)
    if x <= 1:
        return 1
    # 2. Otherwise, return x * fact(x - 1)
    else:
        return x * fact(x-1)


def recursive_sum(arr: List[int]) -> int:
    """
    Sum all elements in array recursively.
    
    Base case: empty array, return 0
    Recursive case: first element + sum of rest
    
    Example:
        >>> recursive_sum([2, 4, 6])
        12
    """
    # TODO: Implement recursive sum
    # 1. If array is empty, return 0 (base case)
    if not arr:
        return 0
    # 2. Otherwise, return arr[0] + recursive_sum(arr[1:])
    else:
        return arr[0] + recursive_sum(arr[1:])


def recursive_count(arr: List) -> int:
    """
    Count elements in array recursively.
    
    Base case: empty array, return 0
    Recursive case: 1 + count of rest
    """
    # TODO: Implement recursive count
    # 1. If array is empty, return 0 (base case)
    if not arr:
        return 0
    # 2. Otherwise, return 1 + recursive_count(arr[1:])
    else:
        return 1 + recursive_count(arr[1:])


def recursive_max(arr: List[int]) -> int:
    """
    Find maximum element recursively.
    
    Base case: single element, return it
    Recursive case: max of (first, max of rest)
    """
    # TODO: Implement recursive max
    # 1. If len(arr) == 1, return arr[0] (base case)
    if len(arr) == 1:
        return arr[0]
    # 2. Get rest_max = recursive_max(arr[1:])
    rest_max = recursive_max(arr[1:])
    # 3. Return arr[0] if arr[0] > rest_max else rest_max
    return arr[0] if arr[0] > rest_max else rest_max
