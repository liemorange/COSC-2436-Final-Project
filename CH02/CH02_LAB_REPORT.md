# Lab 2: Selection Sort

## Student Information
- **Name:** Donghyun Lee
- **Date:** 5/10/2026

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