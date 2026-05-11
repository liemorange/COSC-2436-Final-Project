# 2436 Lab 9 Dijkstra's Algorithm

## Overview
In this assignment, you will implement Dijkstra's Algorithm to find the shortest paths between nodes in a graph. This algorithm is fundamental in computer science for solving shortest path problems, which are essential in network routing, geographical mapping, and various optimization tasks. By completing this assignment, you will gain practical experience with graph algorithms and improve your problem-solving skills.

## Learning Objectives
- Understand and implement Dijkstra's Algorithm.
- Apply Dijkstra's Algorithm to find shortest paths in a graph.
- Demonstrate the algorithm using a dataset of book ratings.

## Requirements
1. Implement the `dijkstra` function to find the shortest path between two nodes in a graph.
2. Ensure the function correctly handles graphs with disconnected nodes.
3. Return both the shortest path and its total cost.

## Getting Started
The starter code is provided in `main.py`. It includes functions to collect nodes and edges from user input, display the graph, and run the main program flow. Your task is to implement the `dijkstra` function, which is currently marked with a TODO comment. Run the code using the Run button in your IDE to test your implementation.

## Implementation Steps
### Implement the `dijkstra` Function
- **TODO:** Implement the `dijkstra` function to find the shortest path between two nodes using Dijkstra's algorithm.
- **Explanation:** This function calculates the shortest path from a start node to an end node in a weighted graph.
- **Complete Code Example:**
  ```python
  def dijkstra(graph, nodes, start, end):
      infinity = float("inf")

      # costs[n] = the cheapest known total cost to reach node n from start
      costs = {n: infinity for n in nodes}
      costs[start] = 0  # It costs nothing to be at the start

      # parents[n] = the node we came from to reach n on the cheapest route
      parents = {n: None for n in nodes}

      # Keep track of nodes whose cheapest path has been finalised
      processed = []

      def find_lowest_cost_node():
          """
          Scan the costs table and return the cheapest unprocessed node.

          Returns None when all reachable nodes have been finalised, which
          signals the main loop to stop.
          """
          lowest = infinity
          result = None
          for n in costs:
              if costs[n] < lowest and n not in processed:
                  lowest = costs[n]
                  result = n
          return result

      # --- Main Dijkstra loop ---
      node = find_lowest_cost_node()
      while node is not None:
          cost = costs[node]  # Cheapest known cost to reach this node

          # Look at every neighbour of the current node
          for neighbor, weight in graph.get(node, {}).items():
              new_cost = cost + weight  # Cost via the current node

              # If this route is cheaper than what we previously knew, update it
              if costs[neighbor] > new_cost:
                  costs[neighbor] = new_cost
                  parents[neighbor] = node  # Remember we came through 'node'

          # Mark this node as done — we won't find a cheaper route to it
          processed.append(node)

          # Move on to the next cheapest unprocessed node
          node = find_lowest_cost_node()

      # If the end node still has infinite cost, it was never reached
      if costs[end] == infinity:
          return None, None

      # --- Reconstruct the path by walking backwards through parents ---
      path = []
      current = end
      while current is not None:
          path.append(current)
          current = parents[current]

      # We built the path from end to start, so reverse it
      path.reverse()

      return path, costs[end]
  ```

## Complete Program
```python
from typing import Optional, Any, List

# Function definitions for get_nodes, get_edges, draw_ascii_graph are omitted for brevity

# Dijkstra's algorithm implementation

def dijkstra(graph, nodes, start, end):
    infinity = float("inf")

    # costs[n] = the cheapest known total cost to reach node n from start
    costs = {n: infinity for n in nodes}
    costs[start] = 0  # It costs nothing to be at the start

    # parents[n] = the node we came from to reach n on the cheapest route
    parents = {n: None for n in nodes}

    # Keep track of nodes whose cheapest path has been finalised
    processed = []

    def find_lowest_cost_node():
        """
        Scan the costs table and return the cheapest unprocessed node.

        Returns None when all reachable nodes have been finalised, which
        signals the main loop to stop.
        """
        lowest = infinity
        result = None
        for n in costs:
            if costs[n] < lowest and n not in processed:
                lowest = costs[n]
                result = n
        return result

    # --- Main Dijkstra loop ---
    node = find_lowest_cost_node()
    while node is not None:
        cost = costs[node]  # Cheapest known cost to reach this node

        # Look at every neighbour of the current node
        for neighbor, weight in graph.get(node, {}).items():
            new_cost = cost + weight  # Cost via the current node

            # If this route is cheaper than what we previously knew, update it
            if costs[neighbor] > new_cost:
                costs[neighbor] = new_cost
                parents[neighbor] = node  # Remember we came through 'node'

        # Mark this node as done — we won't find a cheaper route to it
        processed.append(node)

        # Move on to the next cheapest unprocessed node
        node = find_lowest_cost_node()

    # If the end node still has infinite cost, it was never reached
    if costs[end] == infinity:
        return None, None

    # --- Reconstruct the path by walking backwards through parents ---
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parents[current]

    # We built the path from end to start, so reverse it
    path.reverse()

    return path, costs[end]


def main():
    """
    Entry point — orchestrates the full user interaction flow:

      1. Collect node names
      2. Collect edge weights between node pairs
      3. Display the graph
      4. Ask the user which two nodes to route between
      5. Run Dijkstra's algorithm
      6. Display the graph again with the shortest path highlighted
      7. Print the path and its total cost
    """
    # Step 1: Build the list of nodes
    nodes = get_nodes()
    if len(nodes) < 2:
        print("Need at least 2 nodes. Exiting.")
        return

    # Step 2: Build the edge connections between those nodes
    graph = get_edges(nodes)

    # Step 3: Show the graph before any path is calculated
    draw_ascii_graph(graph, nodes)

    # Step 4: Ask which nodes to route between
    print(f"Nodes: {', '.join(nodes)}")
    start = input("From: ").strip()
    end   = input("To:   ").strip()

    # Validate that both nodes actually exist in the graph
    if start not in nodes:
        print(f"Error: '{start}' is not in the graph.")
        return
    if end not in nodes:
        print(f"Error: '{end}' is not in the graph.")
        return

    # Step 5: Run Dijkstra's algorithm
    path, total_cost = dijkstra(graph, nodes, start, end)

    # Handle the case where no path exists (disconnected graph)
    if path is None:
        print(f"\nNo path found from '{start}' to '{end}'.")
        return

    # Build a set of directed edge tuples that form the shortest path,
    # used by draw_ascii_graph to highlight the correct edges
    path_edges = {(path[i], path[i + 1]) for i in range(len(path) - 1)}

    # Step 6: Re-display the graph with the path highlighted
    draw_ascii_graph(graph, nodes, path_edges=path_edges, start=start, end=end, path=path)

    # Step 7: Print the result summary
    print(f"  Shortest path: {' -> '.join(path)}")
    # Show whole numbers without a trailing .0 for tidiness
    cost_str = int(total_cost) if total_cost == int(total_cost) else total_cost
    print(f"  Total cost:    {cost_str}\n")


# Only run main() when this file is executed directly,
# not when it is imported as a module by another script
if __name__ == "__main__":
    main()
```

## Testing
To test your implementation, run the program using the Run button in your IDE. Follow the prompts to enter nodes and edges, and then find the shortest path between two nodes. Verify that the path and cost are correct.

## Grading Rubric
- Compilation and Syntax Check: 100 pts

## Tips and Hints
- Ensure you initialize the costs of all nodes to infinity, except for the start node, which should be 0.
- Use a helper function to find the lowest cost unprocessed node during each iteration of the main loop.
- Remember to update both the cost and parent for each neighbor if a cheaper path is found.
- After finding the shortest path, reconstruct it by tracing back through the parents dictionary.
- Test your implementation with various graph configurations to ensure it handles all cases, including disconnected graphs.