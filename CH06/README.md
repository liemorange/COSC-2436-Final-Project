[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=23026453&assignment_repo_type=AssignmentRepo)
# Lab 06: 2436 Ch06

## Student Information
- **Name:** Donghyun Lee
- **Date:** 3/8/2026

## Key Concepts
[Explain the main concepts from this lab in your own words] To understand BFS and implement the codes by using the exercise of finding the shortest path in Texas cities.  

## What I Learned
[Describe what you learned while completing this lab] I learned using there is a new built-in data structures sets, queue, tuple, and set.

## Challenges
[What was the most difficult part? How did you solve it?] From the middle, I was completely lost when I had to use tuple, as AI brought it up and deque fuction with a tuple of a tuple and a list inside a list of deque() fuction .

## Reflection Questions
1. [Answer the reflection questions from the instructions file] 

1. Why does BFS use a queue instead of a stack?
BFS and queue both use First In First Out (FIFO). If I use stack, it is like Last In First Out (LIFO). If we use stack, the computer goes very deep into one hole and forgets the neighbors. BFS wants to see all neighbors first, so it use queue to keep them in order.
2. What's the difference between BFS shortest path and actual shortest distance?
BFS shortest path only means fewest jumps.Maybe 2 jumps are 100 miles each. Actual shortest distance would care about something like miles or traffic. BFS is only smart for shortest distance if every jump is same distance, etc. If the weights are different, BFS is inefficient and we need Dijkstra.
3. When would you use BFS vs DFS?
BFS when the answer is probably close to the start. Or if you need the shortest jumps and DFS when the answer is very deep or you want to see the whole tree.
```
---
*Complete this lab report after finishing the coding portion. Your final commit should include both working code and a completed lab report.*
