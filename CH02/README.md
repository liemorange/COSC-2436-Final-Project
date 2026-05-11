[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=22675709&assignment_repo_type=AssignmentRepo)
# Lab 02: Selection Sort

## Overview
Implement selection sort and understand arrays vs linked lists.

## Learning Objectives
- Implement selection sort O(n²)
- Understand array vs linked list tradeoffs
- Analyze algorithm complexity

## Files to Complete
- `sort.py` - Implement `find_smallest()` and `selection_sort()` functions

## Instructions

### Part 1: Implement find_smallest
Find the index of the smallest element in a list starting from a given position.

### Part 2: Implement selection_sort
Use find_smallest to implement selection sort from Chapter 2.

### Part 3: Run Tests
```bash
python -m pytest tests/ -v
```

---

## Lab Report

### Student Information
- **Name:** Donghyun Lee
- **Date:** 2/14/2026

### Algorithm Analysis

#### Selection Sort
- **Time Complexity:** O(?) It is O(n^2) because for each element in the list you may have to sacn the rest of the list, which makes it n*n process.   
- **How it works:** [Your explanation] My explanation of the time being complexity O(n^2) to sort is because there is a loop within a loop in the selection sort. The first algorithm starting from the first to last element and there is the second algorithm within to go through the other elements not sorted, that scans the smallest or the largest element to swap the place with that element. 

#### Arrays vs Linked Lists

| Operation | Array | Linked List | Why? |
|-----------|-------|-------------|------|
| Read      |  O(1) |     O(n)    |   Arrays store memory contiguosly when linked lists store using pointers.  |
| Insert    |  O(n) |     O(1)    |   Arrays move all the other elements' place accordingly to the inserted element in the middle compared to linked lists using pointers.  |
| Delete    |  O(n) |     O(1)    |   Same as inserting, the rest of values in arrays need to move accordingly to the deleted place with the process that can take O(n) time complexity when moving all the elements to the place.   |

### Reflection Questions

1. Why is selection sort O(n²)? Selection sort's time complexity is O(n^2) bacause there is the first loop to go through each element in the list, and within the loop there is another loop that scans the rest of the unsorted values in the array to swap the place if it is the smallest or the largest element.

2. When would you choose a linked list over an array? When I have to insert and delete repeatedly to the list so the size of the list changes frequently, and when there is less need of accessing to the values. 
