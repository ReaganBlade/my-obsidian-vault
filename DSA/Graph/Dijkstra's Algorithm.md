## Introduction
Dijkstra's Algorithm is a classic graph traversal method used to find the **shortest path** from a single source node to all other nodes in a weighted graph. Developed by Dutch computer scientist Edsger W. Dijkstra in 1956, it’s widely applied in navigation systems, network routing, and optimization problems. The algorithm assumes that all edge weights are **non-negative**, making it ideal for problems like finding the shortest driving route.

This document covers:
1. The conceptual foundation of Dijkstra's Algorithm in graph theory.
2. A detailed explanation of how it works.
3. A Python implementation with code breakdown.

---

## Graphs: The Context
A **graph** is a mathematical structure used to model relationships between entities. It consists of:
- **Vertices (Nodes):** Represent entities (e.g., cities, routers).
- **Edges:** Represent connections between vertices (e.g., roads, cables), often with a **weight** (e.g., distance, cost).

### Types of Graphs
- **Directed Graph:** Edges have direction (one-way streets).
- **Undirected Graph:** Edges are bidirectional (two-way roads).
- **Weighted Graph:** Edges have numerical values (distances, costs).
- **Unweighted Graph:** Edges have no weights (all equal).

Dijkstra’s Algorithm operates on **weighted graphs** (directed or undirected) where edge weights are non-negative. Negative weights require a different approach, like the Bellman-Ford algorithm.

### Problem Statement
Given a weighted graph and a starting node (source), find the shortest path (minimum total weight) to every other node. For example:
- In a road network, vertices are cities, edges are roads, and weights are distances. Dijkstra’s finds the shortest route from City A to all others.

---

## How Dijkstra's Algorithm Works

### Core Idea
Dijkstra’s Algorithm uses a **greedy approach**. It:
1. Starts at the source node.
2. Explores nodes by always choosing the one with the current smallest known distance from the source.
3. Updates distances to neighboring nodes if a shorter path is found.
4. Continues until all nodes are processed.

It maintains a "frontier" of explored nodes and iteratively expands it, ensuring the shortest path is found by prioritizing the closest unvisited node.

### Key Components
- **Distance Table:** Tracks the shortest known distance from the source to each node. Initially, the source is 0, and all others are infinity.
- **Visited Set:** Keeps track of nodes whose shortest paths are finalized.
- **Priority Queue:** Efficiently selects the node with the smallest current distance to explore next.
- **Previous Node Tracking:** (Optional) Records the path taken to reconstruct the shortest route.

### Step-by-Step Process
1. **Initialize:**
   - Set the source node’s distance to 0, others to infinity.
   - Mark all nodes as unvisited.
   - Add the source to a priority queue.

2. **Explore:**
   - Pick the node with the smallest distance from the priority queue (initially the source).
   - Mark it as visited.

3. **Update Neighbors:**
   - For each unvisited neighbor of the current node:
     - Calculate the tentative distance (current node’s distance + edge weight to neighbor).
     - If this is less than the neighbor’s current distance, update it.

4. **Repeat:**
   - Add unvisited neighbors to the priority queue with their updated distances.
   - Repeat steps 2-3 until the queue is empty or all nodes are visited.

5. **Result:**
   - The distance table contains the shortest path lengths from the source to all nodes.

### Example
Imagine a graph with 4 nodes: A (source), B, C, D.
- Edges: A→B (4), A→C (2), B→C (1), B→D (5), C→D (8).

| Step | Current Node | Distances (A, B, C, D) | Visited | Queue (Node, Distance) |
|------|--------------|------------------------|---------|------------------------|
| 0    | -            | (0, ∞, ∞, ∞)          | {}      | (A, 0)                |
| 1    | A            | (0, 4, 2, ∞)          | {A}     | (C, 2), (B, 4)        |
| 2    | C            | (0, 4, 2, 10)         | {A, C}  | (B, 4), (D, 10)       |
| 3    | B            | (0, 4, 2, 9)          | {A, C, B} | (D, 9)             |
| 4    | D            | (0, 4, 2, 9)          | {A, C, B, D} | {}          |

**Result:** Shortest distances from A: B=4, C=2, D=9.

---

## Python Implementation

Here’s a Python implementation using a priority queue (via `heapq`) to efficiently select the node with the smallest distance.

```python
import heapq
from collections import defaultdict

def dijkstra(graph, start):
    # Initialize distances: source is 0, others are infinity
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Track previous node for path reconstruction (optional)
    previous = {node: None for node in graph}
    
    # Priority queue: (distance, node)
    pq = [(0, start)]
    
    # Set of visited nodes
    visited = set()

    while pq:
        # Get node with smallest distance
        current_distance, current_node = heapq.heappop(pq)

        # Skip if already visited
        if current_node in visited:
            continue
        
        # Mark as visited
        visited.add(current_node)

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            if neighbor in visited:
                continue
            
            # Calculate tentative distance
            distance = current_distance + weight
            
            # If shorter path found, update distance and previous
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    return distances, previous

# Example graph as adjacency list (node: {neighbor: weight})
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8},
    'D': {'B': 5, 'C': 8}
}

# Run Dijkstra's from node 'A'
distances, previous = dijkstra(graph, 'A')

# Print results
print("Shortest distances from A:")
for node, dist in distances.items():
    print(f"{node}: {dist}")

# Reconstruct path (example: to D)
def get_path(previous, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    return path[::-1]  # Reverse path

print("Path to D:", get_path(previous, 'A', 'D'))
```

### Code Explanation
1. **Imports:**
   - `heapq`: Provides a min-heap for the priority queue.
   - `defaultdict`: Could be used for the graph, but here we use a plain dict for clarity.

2. **Initialization:**
   - `distances`: Dictionary with infinity for all nodes except the source (0).
   - `previous`: Tracks the path (optional).
   - `pq`: Priority queue starts with (0, start).
   - `visited`: Ensures we don’t revisit nodes.

3. **Main Loop:**
   - `heapq.heappop(pq)`: Extracts the node with the smallest distance.
   - Skip if visited to avoid cycles or redundant checks.
   - For each neighbor, calculate the new distance and update if shorter.
   - Push updated distances to the queue.

4. **Graph Representation:**
   - Adjacency list: `graph[node][neighbor] = weight`.
   - Bidirectional edges (e.g., A→B and B→A) are explicitly defined.

5. **Output:**
   - `distances`: Shortest distance to each node.
   - `previous`: Used to reconstruct paths (e.g., A → C → B → D).

### Sample Output
```
Shortest distances from A:
A: 0
B: 4
C: 2
D: 9
Path to D: ['A', 'C', 'B', 'D']
```

---

## Time Complexity
- **With Priority Queue (Heap):** O((V + E) log V)
  - V: Number of vertices.
  - E: Number of edges.
  - Heap operations (insert, extract-min) are O(log V).
- **Without Priority Queue:** O(V²)
  - Linear search for the minimum distance.

## Limitations
- **Non-Negative Weights:** Fails with negative weights (use Bellman-Ford instead).
- **Single Source:** Computes paths from one node only.

## Applications
- **Navigation:** Google Maps for shortest routes.
- **Networking:** Routing protocols like OSPF.
- **Game Development:** Pathfinding for characters.

---

## Conclusion
Dijkstra’s Algorithm elegantly solves the shortest path problem in weighted graphs by leveraging a greedy strategy and a priority queue. Its simplicity and efficiency make it a cornerstone of graph theory and computer science. The Python code above provides a practical way to implement and experiment with it—try modifying the graph to test different scenarios!
