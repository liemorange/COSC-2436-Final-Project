# Lab 6: Breadth-First Search

Implement breadth-first search (BFS) to find shortest paths in graphs. Build a road network connecting Texas cities.

### Objectives
- Understand graph data structures
- Implement BFS algorithm
- Find shortest path (fewest edges)
- Use queues for level-order traversal

### Prerequisites
- Complete Labs 1-5
- Read Chapter 6 in "Grokking Algorithms" (pages 101-120)

---

## 2. Algorithm Background

### Graphs
- **Nodes/Vertices**: Things (cities)
- **Edges**: Connections (roads)
- **Directed vs Undirected**

### BFS Properties
- Explores level by level
- Uses a **queue** (FIFO)
- Finds shortest path by edges
- Time: O(V + E) where V=vertices, E=edges

---

## 3. Your Coding Environment

### Workspace Layout
| Area | What It Does |
|---|---|
| Code Editor (left) | Edit your files using the tabbed editor |
| Terminal (right) | See output when you click the **Run** button |
| AI Tutor (chat panel) | Ask your AI Tutor for help — it knows this lab and can guide you step by step |

### Workflow
1. Edit your code in the editor tabs
2. Click **Run** to execute and see output in the terminal
3. When ready, click **Commit** to save your work to GitHub and trigger the autograder
4. A ✅ (green check) or ❌ (red X) will appear showing whether tests passed

Tip: Commit early and often to track your progress!

---

## 4. Project Structure
```
lab06_bfs/
├── graph.py       # Graph implementation
├── bfs.py         # BFS algorithm
├── main.py        # Main program
└── README.md      # Your lab report
```

---

## 5. Step-by-Step Implementation

### Step 1: Create `graph.py`

```python
"""
Lab 6: Graph Implementation
Adjacency list representation for city road network.
"""
from typing import Dict, List, Set
from collections import defaultdict


class Graph:
    """
    Undirected graph using adjacency list.
    
    Adjacency list: Each node stores list of neighbors
    - Space efficient for sparse graphs
    - O(1) to add edge
    - O(degree) to check if edge exists
    """
    
    def __init__(self):
        # defaultdict creates empty list for new keys
        self.adjacency_list: Dict[str, List[str]] = defaultdict(list)
        self.vertices: Set[str] = set()
    
    def add_vertex(self, vertex: str) -> None:
        """Add a vertex to the graph."""
        self.vertices.add(vertex)
    
    def add_edge(self, v1: str, v2: str) -> None:
        """
        Add undirected edge between v1 and v2.
        For directed graph, only add v1 -> v2.
        """
        self.vertices.add(v1)
        self.vertices.add(v2)
        
        # Undirected: add both directions
        if v2 not in self.adjacency_list[v1]:
            self.adjacency_list[v1].append(v2)
        if v1 not in self.adjacency_list[v2]:
            self.adjacency_list[v2].append(v1)
    
    def get_neighbors(self, vertex: str) -> List[str]:
        """Get all neighbors of a vertex."""
        return self.adjacency_list[vertex]
    
    def has_edge(self, v1: str, v2: str) -> bool:
        """Check if edge exists between v1 and v2."""
        return v2 in self.adjacency_list[v1]
    
    def display(self) -> None:
        """Display the graph structure."""
        print("\nGraph Adjacency List:")
        print("-" * 40)
        for vertex in sorted(self.vertices):
            neighbors = self.adjacency_list[vertex]
            print(f"{vertex}: {neighbors}")
    
    def __len__(self) -> int:
        return len(self.vertices)


def create_texas_road_network() -> Graph:
    """
    Create a simplified Texas highway network.
    Edges represent direct highway connections.
    """
    g = Graph()
    
    # Major highway connections (simplified)
    roads = [
        # I-45 corridor
        ("Houston", "Dallas"),
        
        # I-35 corridor  
        ("Dallas", "Austin"),
        ("Austin", "San Antonio"),
        ("San Antonio", "Laredo"),
        
        # I-10 corridor
        ("Houston", "San Antonio"),
        ("San Antonio", "El Paso"),
        
        # I-20 corridor
        ("Dallas", "Fort Worth"),
        ("Fort Worth", "Lubbock"),
        ("Lubbock", "El Paso"),
        
        # Other connections
        ("Dallas", "Arlington"),
        ("Fort Worth", "Arlington"),
        ("Houston", "Corpus Christi"),
        ("Corpus Christi", "San Antonio"),
        ("Austin", "Killeen"),
        ("Dallas", "Plano"),
        ("Dallas", "Irving"),
        ("Dallas", "Garland"),
        ("Plano", "Frisco"),
        ("Plano", "McKinney"),
        ("Corpus Christi", "Brownsville"),
        ("Brownsville", "McAllen"),
        ("McAllen", "Laredo"),
    ]
    
    for city1, city2 in roads:
        g.add_edge(city1, city2)
    
    return g
```

### Step 2: Create `bfs.py`

```python
"""
Lab 6: Breadth-First Search Implementation
Finds shortest path (by number of edges) in unweighted graph.
"""
from typing import List, Dict, Optional
from collections import deque
from graph import Graph

def bfs_find_path(graph: Graph, start: str, end: str) -> Optional[List[str]]:
    """
    Find shortest path from start to end using BFS.
    
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    
    Returns:
        List of vertices forming the path, or None if no path exists
    """
    # TODO: Implement bfs_find_path
    # 1. Check if start or end is not in graph, return None if not
    # 2. Initialize a queue with (start, [start])
    # 3. Initialize visited set with start
    # 4. While queue is not empty, pop the queue
    # 5. If current vertex is end, return path
    # 6. For each neighbor of current, if not visited, add to queue and visited
    pass  # Remove this and add your code

def bfs_all_reachable(graph: Graph, start: str) -> Dict[str, int]:
    """
    Find all vertices reachable from start and their distances.
    
    Returns:
        Dict mapping vertex -> distance from start
    """
    # TODO: Implement bfs_all_reachable
    # 1. Check if start is not in graph, return empty dict if not
    # 2. Initialize distances dict with start at distance 0
    # 3. Initialize queue with start
    # 4. While queue is not empty, pop queue
    # 5. For each neighbor, if not in distances, set distance and add to queue
    pass  # Remove this and add your code

def bfs_is_connected(graph: Graph, v1: str, v2: str) -> bool:
    """Check if path exists between two vertices."""
    # TODO: Implement bfs_is_connected
    # 1. Use bfs_find_path to check if path exists
    # 2. Return True if path exists, False otherwise
    pass  # Remove this and add your code
```

### Step 3: Create `main.py`

```python
"""
Lab 6: Main Program
Demonstrates BFS on Texas road network.
"""
from graph import Graph, create_texas_road_network
from bfs import bfs_find_path, bfs_all_reachable


def main():
    # =========================================
    # PART 1: Create Road Network
    # =========================================
    print("=" * 60)
    print("PART 1: TEXAS ROAD NETWORK GRAPH")
    print("=" * 60)
    
    roads = create_texas_road_network()
    print(f"\nCreated graph with {len(roads)} cities")
    roads.display()
    
    # =========================================
    # PART 2: Find Shortest Paths
    # =========================================
    print("\n" + "=" * 60)
    print("PART 2: SHORTEST PATH (BFS)")
    print("=" * 60)
    
    # Houston to El Paso
    path = bfs_find_path(roads, "Houston", "El Paso")
    if path:
        print(f"\nRoute: {' → '.join(path)}")
    
    # Houston to McKinney
    print("\n" + "-" * 40)
    path = bfs_find_path(roads, "Houston", "McKinney")
    if path:
        print(f"\nRoute: {' → '.join(path)}")
    
    # =========================================
    # PART 3: Reachability
    # =========================================
    print("\n" + "=" * 60)
    print("PART 3: DISTANCES FROM HOUSTON")
    print("=" * 60)
    
    distances = bfs_all_reachable(roads, "Houston")
    
    print("\nCities by distance (edges) from Houston:")
    for dist in range(max(distances.values()) + 1):
        cities_at_dist = [c for c, d in distances.items() if d == dist]
        if cities_at_dist:
            print(f"  {dist} edge(s): {', '.join(sorted(cities_at_dist))}")
    
    # =========================================
    # PART 4: Key Concepts
    # =========================================
    print("\n" + "=" * 60)
    print("PART 4: BFS KEY CONCEPTS")
    print("=" * 60)
    print("""
    Why BFS finds shortest path:
    1. Explores ALL nodes at distance 1 first
    2. Then ALL nodes at distance 2
    3. And so on...
    
    First time we reach destination = shortest path!
    
    BFS uses a QUEUE (FIFO):
    - First In, First Out
    - Process nodes in order they were discovered
    
    Time Complexity: O(V + E)
    - Visit each vertex once: O(V)
    - Check each edge once: O(E)
    
    Note: BFS finds shortest path by NUMBER OF EDGES.
    For weighted graphs (actual distances), use Dijkstra's (Lab 9)!
    """)


if __name__ == "__main__":
    main()
```

---

## 6. Testing Your Code

### Run Your Code
Click **Run** to execute and check the output.

### Submit for Grading
Click **Commit**, enter a message, and look for ✅ or ❌.

Expected output:
```
Graph Adjacency List:
----------------------------------------
Arlington: ['Dallas', 'Fort Worth']
Austin: ['Dallas', 'San Antonio', 'Killeen']
Brownsville: ['Corpus Christi', 'McAllen']
Corpus Christi: ['Houston', 'San Antonio', 'Brownsville']
Dallas: ['Houston', 'Austin', 'Fort Worth', 'Arlington', 'Plano', 'Irving', 'Garland']
El Paso: ['San Antonio', 'Lubbock']
Fort Worth: ['Dallas', 'Lubbock', 'Arlington']
Frisco: ['Plano']
Garland: ['Dallas']
Houston: ['Dallas', 'San Antonio', 'Corpus Christi']
Irving: ['Dallas']
Killeen: ['Austin']
Laredo: ['San Antonio', 'McAllen']
Lubbock: ['Fort Worth', 'El Paso']
McAllen: ['Brownsville', 'Laredo']
McKinney: ['Plano']
Plano: ['Dallas', 'Frisco', 'McKinney']
San Antonio: ['Austin', 'Laredo', 'El Paso', 'Houston', 'Corpus Christi']


BFS from 'Houston' to 'El Paso':
----------------------------------------
Level 0: Visiting 'Houston'
Level 1: Visiting 'Dallas'
Level 1: Visiting 'San Antonio'
Level 1: Visiting 'Corpus Christi'
Level 2: Visiting 'Austin'
Level 2: Visiting 'Laredo'
Level 2: Visiting 'El Paso'

Found path with 2 edges!

Route: Houston → San Antonio → El Paso

----------------------------------------

BFS from 'Houston' to 'McKinney':
----------------------------------------
Level 0: Visiting 'Houston'
Level 1: Visiting 'Dallas'
Level 1: Visiting 'San Antonio'
Level 1: Visiting 'Corpus Christi'
Level 2: Visiting 'Austin'
Level 2: Visiting 'Fort Worth'
Level 2: Visiting 'Arlington'
Level 2: Visiting 'Plano'
Level 2: Visiting 'Irving'
Level 2: Visiting 'Garland'
Level 3: Visiting 'Laredo'
Level 3: Visiting 'El Paso'
Level 3: Visiting 'Frisco'
Level 3: Visiting 'McKinney'

Found path with 3 edges!

Route: Houston → Dallas → Plano → McKinney

Cities by distance (edges) from Houston:
  0 edge(s): Houston
  1 edge(s): Corpus Christi, Dallas, San Antonio
  2 edge(s): Arlington, Austin, Fort Worth, Garland, Irving, Laredo, Plano
  3 edge(s): El Paso, Frisco, Killeen, Lubbock, McKinney
  4 edge(s): Brownsville, McAllen

PART 4: BFS KEY CONCEPTS
============================================================

    Why BFS finds shortest path:
    1. Explores ALL nodes at distance 1 first
    2. Then ALL nodes at distance 2
    3. And so on...

    First time we reach destination = shortest path!

    BFS uses a QUEUE (FIFO):
    - First In, First Out
    - Process nodes in order they were discovered

    Time Complexity: O(V + E)
    - Visit each vertex once: O(V)
    - Check each edge once: O(E)

    Note: BFS finds shortest path by NUMBER OF EDGES.
    For weighted graphs (actual distances), use Dijkstra's (Lab 9)!
```

---

## 7. Autograding

| Test | Points | What It Checks |
|---|---|---|
| Compilation and Syntax Check | 10 | Code compiles without errors |
| Functional Test | 90 | Correctness of BFS operations and output |

Total: 100 points

---

## 8. Lab Report
Click the README.md tab and fill in your lab report.

```markdown
# Lab 6: Breadth-First Search

## Student Information
- **Name:**  Donghyun Lee
- **Date:**  05/10/26

## Graph Concepts

### Adjacency List Representation
[Explain how the graph is stored]

### BFS Algorithm Steps
1. [Step 1] add the start node to the queue
2. [Step 2] deque it once done and mark it visited
3. [Continue...] repeat it until finding the target

## Test Results

| Start | End | Path | Edges |
|-------|-----|------|-------|
| Houston | El Paso | Houston, Dallas, EL Paso | 2 |
| Houston | McKinney | Houston, Dallas, McKinney| 2 |
| Dallas | Laredo |Dallas, Houston, San ANtonio, Laredo | 3 | 

## Reflection Questions

1. Why does BFS use a queue instead of a stack?
Queue is first in last out so it goes through neighbors in the same way would a person travel but stack is first in last out. 
2. What's the difference between BFS shortest path and actual shortest distance?
Well there should be considerations on things like actual distance than just having fewer nodes to travel.
3. When would you use BFS vs DFS?
BFS when I need to find the shorted path without considering other factors but only the connection and DFS when I waant to know every path. 
```

---

## 9. Submission Checklist
- [ ] All functions implemented
- [ ] Click Run — output matches expected
- [ ] Click Commit — autograder shows green check
- [ ] Lab report completed in README.md
- [ ] Final commit with completed lab report
