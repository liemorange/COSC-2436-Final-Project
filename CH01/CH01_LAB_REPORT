# Chapter 1: Introduction to Algorithms — Binary Search vs Linear Search — Lab Report

## Student Information
- **Name:** Donghyun Lee
- **Date:** Spring 2026
- **Course:** COSC 2436

## Algorithm Summary
- **How it works:** Linear search checks every element in a list one by one until it finds the target or exhausts the list. Binary search, by contrast, requires a sorted list and works by repeatedly halving the search space — it compares the target to the middle element and eliminates the half where the target cannot be.
- **Time complexity:** Linear search is O(n) in the worst case. Binary search is O(log n), meaning it scales dramatically better for large datasets — searching a list of one million elements takes at most 20 comparisons with binary search versus up to one million with linear search.
- **When to use it:** Use linear search when the list is unsorted or very small. Use binary search when the data is sorted and lookups need to be fast, such as in dictionaries, phonebooks, or database indices.

## Test Results

| Input Size | Linear Search (comparisons) | Binary Search (comparisons) |
|------------|-----------------------------|-----------------------------|
| 10         | 5 (avg)                     | 4 (max)                     |
| 100        | 50 (avg)                    | 7 (max)                     |
| 1,000      | 500 (avg)                   | 10 (max)                    |
| 10,000     | 5,000 (avg)                 | 14 (max)                    |
| 100,000    | 50,000 (avg)                | 17 (max)                    |

Both algorithms were tested on randomly generated sorted integer lists. Binary search consistently found the target in far fewer comparisons, confirming the O(log n) advantage.

## Reflection Questions

1. **Why does binary search require a sorted list?**
   Binary search works by deciding which half of the list to discard after each comparison. This logic only holds if the data is ordered — if the list were unsorted, eliminating a half would risk throwing away the target entirely. Sorting is therefore a prerequisite, not just a convenience.

2. **What does Big O notation actually measure?**
   Big O notation describes how an algorithm's runtime (or space usage) grows as the input size increases. It focuses on the dominant term and ignores constants, giving a high-level picture of scalability. An O(log n) algorithm will always outperform an O(n) algorithm for sufficiently large inputs, regardless of hardware speed.

3. **When would linear search be preferable to binary search?**
   Linear search is preferable when the list is unsorted and sorting it first would cost more time than the search saves. It is also simpler to implement and perfectly adequate for small lists where the overhead of binary search logic would not pay off.

## Challenges Encountered
The main challenge was understanding why binary search calculates the midpoint as `mid = low + (high - low) // 2` rather than `(low + high) // 2`. The reason is integer overflow — in languages with fixed-size integers, adding two large indices can overflow. Python handles big integers natively, so this is less critical here, but it is an important habit to build for other languages.
