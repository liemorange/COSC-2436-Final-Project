# Chapter 1 Lab Report: Binary Search

## Student Information
- **Name:** Donghyun Lee
- **Date:** 5/10/2026
- **Course:** COSC 2436

## Algorithm Summary

### Linear Search
[Explain how linear search works in plain English. Include time complexity and when to use it.]
It checks every item in the list sequentially and it ends if it finds the value it was looking for or it ends if the list ends. It has O(n) time complexity and is used mostly on unsorted lists where no binary searches and such are unapplicable.
### Binary Search
[Explain how binary search works in plain English. Include time complexity and when to use it.]
It checks the middle item in a sorted list making the search portioned left smaller values half and right bigger values half, and searches to the bigger or smaller half constantly until the middle item matches. O(log n) is the time colexity of binary search.  
## Test Results

[Paste the output from your program here, showing the timing comparisons between linear and binary search]

      
      Binary Search vs Linear Search Time Comparison
      ================================================
      Searching in a sorted list of 128 numbers
      
      Searching for: 1
      Linear search time: 0.00000238 seconds
      Binary search time: 0.00000286 seconds
      Linear search result: 0
      Binary search result: 0
      Binary search is 0.83x faster
      
      Searching for: 64
      Linear search time: 0.00006413 seconds
      Binary search time: 0.00000143 seconds
      Linear search result: 63
      Binary search result: 63
      Binary search is 44.83x faster
      
      Searching for: 128
      Linear search time: 0.00000358 seconds
      Binary search time: 0.00000167 seconds
      Linear search result: 127
      Binary search result: 127
      Binary search is 2.14x faster
      
      Searching for: 50
      Linear search time: 0.00000191 seconds
      Binary search time: 0.00000143 seconds
      Linear search result: 49
      Binary search result: 49
      Binary search is 1.33x faster
      
      Searching for: 100
      Linear search time: 0.00000238 seconds
      Binary search time: 0.00000072 seconds
      Linear search result: 99
      Binary search result: 99
      Binary search is 3.33x faster
      
      Searching for: 25
      Linear search time: 0.00000072 seconds
      Binary search time: 0.00000072 seconds
      Linear search result: 24
      Binary search result: 24
      Binary search is 1.00x faster
      
      Searching for: 75
      Linear search time: 0.00000262 seconds
      Binary search time: 0.00000191 seconds
      Linear search result: 74
      Binary search result: 74
      Binary search is 1.38x faster
      
      Searching for: 10
      Linear search time: 0.00000143 seconds
      Binary search time: 0.00000143 seconds
      Linear search result: 9
      Binary search result: 9
      Binary search is 1.00x faster
      
      Searching for: 90
      Linear search time: 0.00000286 seconds
      Binary search time: 0.00000167 seconds
      Linear search result: 89
      Binary search result: 89
      Binary search is 1.71x faster
      
      Searching for: 200
      Linear search time: 0.00000286 seconds
      Binary search time: 0.00000095 seconds
      Linear search result: None
      Binary search result: None
      Binary search is 3.00x faster
      
      Lab Challenge Answer:
      Maximum steps for binary search in 128 items:
      log2(128) = 7 steps maximum
