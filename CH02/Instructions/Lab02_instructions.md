# Lab 2: Selection Sort

## 1. Introduction and Objectives

### Overview
Implement selection sort and explore arrays vs linked lists. You'll sort cities by population and understand O(n²) complexity.

### Learning Objectives
- Implement selection sort algorithm
- Understand array vs linked list tradeoffs
- Analyze O(n²) time complexity
- Work with Python lists and sorting

### Prerequisites
- Complete Lab 1
- Read Chapter 2 in "Grokking Algorithms" (pages 21-39)

---

## 2. Algorithm Background

### Selection Sort - O(n²)
1. Find the smallest element
2. Swap it to the front
3. Repeat for remaining elements

### Arrays vs Linked Lists

| Operation | Array | Linked List |
|-----------|-------|-------------|
| Read | O(1) | O(n) |
| Insert | O(n) | O(1) |
| Delete | O(n) | O(1) |

Python lists are actually dynamic arrays!

---

## 3. Project Structure

```
lab02_selection_sort/
├── sort.py        # Sort algorithm implementations
├── linked_list.py # Simple linked list implementation
├── main.py        # Main program
└── README.md      # Your lab report
```

---

## 4. Step-by-Step Implementation

### Step 1: Create `sort.py`

```python
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
    smallest_idx = start
    smallest_val = key(arr[start])
    
    for i in range(start + 1, len(arr)):
        if key(arr[i]) < smallest_val:
            smallest_val = key(arr[i])
            smallest_idx = i
    
    return smallest_idx


def selection_sort(arr: List[Dict], key: Callable, reverse: bool = False) -> List[Dict]:
    """
    Sort list using selection sort algorithm.
    Time Complexity: O(n²)
    Space Complexity: O(1) - in-place sort
    
    Args:
        arr: List to sort
        key: Function to extract comparison value
        reverse: If True, sort descending
    
    Returns:
        Sorted list (same list, modified in place)
    """
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    # Create a copy to avoid modifying original
    result = arr.copy()
    
    for i in range(n - 1):
        # Find smallest (or largest if reverse) in remaining portion
        if reverse:
            # Find largest
            extreme_idx = i
            extreme_val = key(result[i])
            for j in range(i + 1, n):
                comparisons += 1
                if key(result[j]) > extreme_val:
                    extreme_val = key(result[j])
                    extreme_idx = j
        else:
            # Find smallest
            extreme_idx = i
            extreme_val = key(result[i])
            for j in range(i + 1, n):
                comparisons += 1
                if key(result[j]) < extreme_val:
                    extreme_val = key(result[j])
                    extreme_idx = j
        
        # Swap if needed
        if extreme_idx != i:
            result[i], result[extreme_idx] = result[extreme_idx], result[i]
            swaps += 1
    
    print(f"Selection Sort: {comparisons} comparisons, {swaps} swaps")
    return result


def python_builtin_sort(arr: List[Dict], key: Callable, reverse: bool = False) -> List[Dict]:
    """
    Python's built-in sort for comparison.
    Time Complexity: O(n log n) - Timsort algorithm
    """
    result = arr.copy()
    result.sort(key=key, reverse=reverse)
    print("Python Built-in Sort: O(n log n) - Timsort")
    return result
```

### Step 2: Create `linked_list.py`

```python
"""
Lab 2: Simple Linked List Implementation
Demonstrates linked list concepts from Chapter 2.
"""
from typing import Any, Optional


class Node:
    """A node in the linked list."""
    
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional['Node'] = None
    
    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    """
    Simple singly linked list.
    
    Insert: O(1) at head, O(n) at tail
    Delete: O(1) at head, O(n) elsewhere
    Search: O(n)
    Access by index: O(n)
    """
    
    def __init__(self):
        self.head: Optional[Node] = None
        self.size = 0
    
    def insert_at_head(self, data: Any) -> None:
        """Insert at beginning - O(1)"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert_at_tail(self, data: Any) -> None:
        """Insert at end - O(n)"""
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.size += 1
    
    def delete_at_head(self) -> Optional[Any]:
        """Delete from beginning - O(1)"""
        if self.head is None:
            return None
        
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data
    
    def search(self, target: Any, key=lambda x: x) -> Optional[Node]:
        """Search for element - O(n)"""
        current = self.head
        comparisons = 0
        
        while current:
            comparisons += 1
            if key(current.data) == target:
                print(f"LinkedList Search: Found in {comparisons} comparisons")
                return current
            current = current.next
        
        print(f"LinkedList Search: Not found after {comparisons} comparisons")
        return None
    
    def to_list(self) -> list:
        """Convert to Python list for display."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def __len__(self):
        return self.size
    
    def __repr__(self):
        return f"LinkedList({self.to_list()})"
```

### Step 3: Create `main.py`

```python
"""
Lab 2: Main Program
Demonstrates selection sort and array vs linked list.
"""
import json
import time
from sort import selection_sort, python_builtin_sort
from linked_list import LinkedList


def load_cities(filename: str) -> list:
    """Load cities from JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)


def main():
    # Load city data
    cities = load_cities('../data/cities.json')
    print(f"Loaded {len(cities)} cities\n")
    
    # =========================================
    # PART 1: Selection Sort
    # =========================================
    print("=" * 60)
    print("PART 1: SELECTION SORT")
    print("=" * 60)
    
    # Sort by population (ascending)
    print("\nSorting cities by population (smallest first)...")
    sorted_asc = selection_sort(cities, key=lambda x: x['population'])
    
    print("\nTop 5 smallest cities:")
    for city in sorted_asc[:5]:
        print(f"  {city['name']}: {city['population']:,}")
    
    # Sort by population (descending)
    print("\nSorting cities by population (largest first)...")
    sorted_desc = selection_sort(cities, key=lambda x: x['population'], reverse=True)
    
    print("\nTop 5 largest cities:")
    for city in sorted_desc[:5]:
        print(f"  {city['name']}: {city['population']:,}")
    
    # Compare with Python's built-in sort
    print("\n" + "-" * 40)
    print("Comparison with Python's built-in sort:")
    python_builtin_sort(cities, key=lambda x: x['population'])
    
    # =========================================
    # PART 2: Array vs Linked List
    # =========================================
    print("\n" + "=" * 60)
    print("PART 2: ARRAY VS LINKED LIST")
    print("=" * 60)
    
    # Demonstrate array (Python list) operations
    print("\n--- Python List (Array) Operations ---")
    
    city_names = [c['name'] for c in cities]
    
    # Access by index - O(1)
    start = time.time()
    middle_city = city_names[len(city_names) // 2]
    elapsed = (time.time() - start) * 1000000  # microseconds
    print(f"Array access by index [10]: '{middle_city}' - O(1) - {elapsed:.2f} µs")
    
    # Insert at beginning - O(n)
    start = time.time()
    city_names_copy = city_names.copy()
    city_names_copy.insert(0, "New City")
    elapsed = (time.time() - start) * 1000000
    print(f"Array insert at beginning: O(n) - {elapsed:.2f} µs")
    
    # Demonstrate linked list operations
    print("\n--- Linked List Operations ---")
    
    linked_cities = LinkedList()
    for city in cities:
        linked_cities.insert_at_tail(city)
    
    print(f"Created linked list with {len(linked_cities)} cities")
    
    # Insert at head - O(1)
    start = time.time()
    linked_cities.insert_at_head({"name": "New City", "population": 0})
    elapsed = (time.time() - start) * 1000000
    print(f"LinkedList insert at head: O(1) - {elapsed:.2f} µs")
    
    # Search - O(n)
    print("\nSearching for 'Dallas' in linked list...")
    linked_cities.search("Dallas", key=lambda x: x['name'])
    
    # =========================================
    # PART 3: Big O Comparison
    # =========================================
    print("\n" + "=" * 60)
    print("PART 3: BIG O SUMMARY")
    print("=" * 60)
    
    print("""
    Selection Sort: O(n²)
    - For 20 cities: ~190 comparisons
    - For 1000 cities: ~500,000 comparisons
    - For 1,000,000 cities: ~500 billion comparisons!
    
    Python's Timsort: O(n log n)  
    - For 20 cities: ~86 comparisons
    - For 1000 cities: ~10,000 comparisons
    - For 1,000,000 cities: ~20 million comparisons
    
    Array vs Linked List:
    ┌───────────┬─────────┬─────────────┐
    │ Operation │  Array  │ Linked List │
    ├───────────┼─────────┼─────────────┤
    │ Read      │  O(1)   │    O(n)     │
    │ Insert    │  O(n)   │    O(1)*    │
    │ Delete    │  O(n)   │    O(1)*    │
    └───────────┴─────────┴─────────────┘
    * O(1) only at head; O(n) to find position
    """)


if __name__ == "__main__":
    main()
```

---

## 5. Expected Output

```
Loaded 20 cities

============================================================
PART 1: SELECTION SORT
============================================================

Sorting cities by population (smallest first)...
Selection Sort: 190 comparisons, 19 swaps

Top 5 smallest cities:
  McAllen: 142,210
  Pasadena: 151,950
  Killeen: 153,095
  Brownsville: 183,392
  McKinney: 195,308

... [more output]
```

---

## 6. Lab Report Template

Create `README.md`:

```markdown
# Lab 2: Selection Sort

## Student Information
- **Name:** [Your Name]
- **Date:** [Date]

## Algorithm Summary

### Selection Sort
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **How it works:** [Your explanation] it chooses one value and compare with every other values to find the value it is looking for.

## Array vs Linked List Analysis

| Operation | Array | Linked List | Why? |
|-----------|-------|-------------|------|
| Read      | O(1)  | O(n)        |   it has to sequentially gothrough every node to find the value   |
| Insert    | O(n)  | O(1)        |   Just tie it to the next node   |
| Delete    | O(n)  | O(1)        |   Delete the node and connect it to the next node   |

## Test Results
[Document your sorting results]

## Reflection Questions

1. Why is selection sort O(n²)?
Becuase it has two loops, one is outer loop going through to find the minimum value and the inner loop going through comparing with that value. 
2. When would you choose a linked list over an array?
Using linked lists when total number of elements are not known and the list changes a lot. 
3. Why does Python use arrays (lists) as the default sequence type?
Because it has random accenss, it can jump right away to the value and there is aptial locality that could be benefited from that. 
```

---

## 7. Submission

1. Save all files in `lab02_selection_sort/`
2. Complete your lab README
3. Commit and push to GitHub
