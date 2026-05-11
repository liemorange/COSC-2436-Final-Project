[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=22788885&assignment_repo_type=AssignmentRepo)
# Lab 04: Quicksort

## Student Information
- **Name:** Donghyun Lee
- **Date:** 2/20/2026

## Quicksort Concepts

### Divide and Conquer
[Explain how quicksort uses divide-and-conquer in your own words]

### The Three Steps
1. **Choose pivot:** a pivot value, the first number in this case, will be used to seperate the array into two partitions. 
2. **Partition:** Once the pivot is picked, the numbers after pivot will be divided into two partition lists of less and greater values.  
3. **Recurse and combine:** Finish recursion after reaching the base case of having no more values to partition, and start combining back the partitions and pivots back into a sorted list.

## Tracing Quicksort

### Trace: quicksort([3, 5, 2, 1, 4])
[Draw out each recursive call step by step, showing the pivot, less, and greater at each level]
quicksort([3,5,2,1,4])
  pivot: 3
  less: [2,1]
  greater: [5,4]
  return quicksort([2, 1]) + [3] + quicksort([5,4])

  quicksort([2,1])
      pivot: 2
      less: [1]
      greater: []
      return quicksort([1]) + [2] + quicksort([])
        quicksort([1]) -> return [1]
        quicksort([])  -> return []
      result: [1, 2]

  quicksort([5,4])
      pivot: 5
      less: [4]
      greater: []
      return quicksort([4]) + [5] + quicksort([])
        quicksort([4]) -> return [4]
        quicksort([])  -> return []
      result: [4,5]

return [1, 2] + [3] + [4, 5]

Result: [1, 2, 3, 4, 5]

## Complexity Analysis

| Case | Time Complexity | Why? |
|------|----------------|------|
| Best | O(n log n) |  The pivot if it is the exact middle value to divide partitions equally and takes n times searching through array multiplied with log n number of recursion levels. |
| Average | O(n log n) | On average, pivots splits data effectively although it might not be the best case slower than the best case. |
| Worst | O(n²) | In the worst case when the pivot is always the worst case of being the smallest or the largerst value, all the pivots have to go through all the values therefore it takes n times n time complexity|

## Reflection Questions

1. What happens if the array is already sorted and you always pick the first element as pivot? It becomes the worst case and takes time complexity of O(n^2).

2. How could you improve pivot selection to avoid worst-case performance? Picking from the other places would help, like picking the pivot number from the middle or from a random number. 

3. How does quicksort compare to other sorting algorithms you know (e.g., bubble sort, merge sort)? It is effective as it has better time complexity for the average time than bubble sort and merge sort.

4. Why do we use `array[1:]` instead of `array` when building the less and greater lists? Because the recursion would not end as it keeps including itself in the greater list if not in less list. The pivot value is supposed to be used for comparison with other values not itself.
