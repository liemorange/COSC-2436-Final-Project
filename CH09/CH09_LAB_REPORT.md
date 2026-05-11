# Chapter 9: Dijkstra's Algorithm (Shortest Path) — Lab Report

## Student Information
- **Name:** Donghyun Lee
- **Date:** 05/10/2026

## Algorithm Summary
- **How it works:** You start at the source with cost 0, everything else is infinity and each step you pick the cheapest unvisited item, check if going through it gives any neighbors a better price, and update if so. Keep doing that until you reach the destination.
- **Time complexity:** O((V + E) log V) for min-heap and O(V²) array based approach.
- **When to use it:** Dijkstra's algorithm is used when you need the shortest path in a weighted graph and none of the weights are negative like GPS.

## Test Results

**Test graph (weighted, directed):**

=== Dijkstra's Shortest Path ===

Enter node names one per line.
Type 'done' when finished.

Node: A
  Added: A
Node: B
  Added: B
Node: C
  Added: C
Node: D
  Added: D
Node: done

For each pair of nodes, enter the edge weight if connected, or press Enter to skip.

  A <--> B  (weight or Enter to skip): 3
    Added: A <--3--> B
  A <--> C  (weight or Enter to skip): 2
    Added: A <--2--> C
  A <--> D  (weight or Enter to skip): 1
    Added: A <--1--> D
  B <--> C  (weight or Enter to skip): 4
    Added: B <--4--> C
  B <--> D  (weight or Enter to skip): 2
    Added: B <--2--> D
  C <--> D  (weight or Enter to skip): 3
    Added: C <--3--> D

────────────────────────────────────────────────────
  GRAPH
────────────────────────────────────────────────────
           (A)  <->  3       (B)
           (A)  <->  2       (C)
           (A)  <->  1       (D)
           (B)  <->  4       (C)
           (B)  <->  2       (D)
           (C)  <->  3       (D)
────────────────────────────────────────────────────

Nodes: A, B, C, D
From: A
To:   C

────────────────────────────────────────────────────
  GRAPH
────────────────────────────────────────────────────
           [A]  <->  3       (B)
           [A]  <=>  2       [C]
           [A]  <->  1       (D)
           (B)  <->  4       [C]
           (B)  <->  2       (D)
           [C]  <->  3       (D)
────────────────────────────────────────────────────
  [node] = on shortest path    (node) = not on path    <=> = path edge    <-> = other edge

  Shortest path: A -> C
  Total cost:    2

The algorithm correctly identified that the path A → C → D (cost 4) is shorter than A → B → D (cost 8), demonstrating how it avoids greedy shortest-first errors.

## Reflection Questions

Why does Dijkstra's algorithm fail on graphs with negative edge weights?
Because it assumes once you finalize a node's distance you're done with it. But a negative edge somewhere could make that distance wrong after the fact. So it just breaks. Bellman-Ford deals with this by not making that assumption

What role does the priority queue play in Dijkstra's efficiency?
It just grabs the cheapest node for you automatically  instead of you having to scan through everything yourself. Saves a lot of unnecessary work.

How does Dijkstra's algorithm relate to BFS from Chapter 6?
Pretty much the  same thing honestly, just BFS doesn't care about weights so a regular queue is enough. Dijkstra needs a priority queue because edges have different costs.

## Challenges Encountered
I kept getting errors and didn't know why for a while and found out I had to set up the beginning as infinite. 
