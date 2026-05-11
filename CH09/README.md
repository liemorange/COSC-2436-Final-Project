[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=23520342&assignment_repo_type=AssignmentRepo)
Lab Report — Dijkstra's Shortest Path

Student Information

Name: Donghyun Lee
Date: 4/11/2026
Algorithm Analysis: Dijkstra's Algorithm

What type of graph does this program build? [Your answer — directed/undirected, weighted/unweighted]  Undirected and weighted, edges go both ways and each has a cost.
Why must all edge weights be non-negative for Dijkstra's to work? [Your explanation] use Bellman-Ford for negatives, Dijkstra for non-negatives because it's faster.
Time Complexity (with simple array scan for min-node): O(?) O(V^2)
Time Complexity (with a min-heap/priority queue): O(?) O((V+E)log V)
Core Data Structures

Structure	Variable Name	What It Stores
Adjacency dict	graph	
Cost table	costs	
Parent table	parents	
Visited list	processed	
Algorithm Trace

Given nodes A, B, C, D and edges A-B(1), A-C(4), B-C(2), B-D(6), C-D(3), trace Dijkstra's from A to D:

Iteration	Current Node	costs[A]	costs[B]	costs[C]	costs[D]	processed
Init	—					
1						
2						
3						
4						
Shortest path A to D: [Your answer]
Total cost: [Your answer]

Reflection Questions

Why does the algorithm initialize all node costs to infinity except the start node?
Becuase we are finding the minimum even if it is close to infinity it still has to find at least one that is smaller than infinity. So every node starts as unreachable and only gets updated when a real path is found through the algorithm.

Why do we store edges in both directions (graph[a][b] and graph[b][a])? What would break if we only stored one direction?
Because the graph is undirected — if you only store one direction you can only travel one way and would miss valid paths.

The find_lowest_cost_node() function scans all nodes linearly. How would using a priority queue (min-heap) improve performance, and why does it matter for large graphs?
A min-heap always has the cheapest node ready at the top so you don't have to scan every node each time, which matters a lot when the graph has thousands of nodes.

If a negative edge weight were introduced (e.g., A-B with weight -3), explain how Dijkstra's algorithm could produce an incorrect result. What algorithm handles negative weights?
Dijkstra marks a node done and never revisits it, so a negative edge found later could offer a cheaper path that gets ignored, giving the wrong answer. Bellman-Ford handles negative weights.

How does the parents dictionary allow path reconstruction? Why do we reverse the path at the end?
It tracks where we came from at each node, so we trace backwards from end to start to rebuild the path, then reverse it to get the correct order.

What happens when the source and destination are in disconnected components of the graph? How does the code detect this?
The end node cost stays infinity because it was never reached, and the code checks for that and returns None.
