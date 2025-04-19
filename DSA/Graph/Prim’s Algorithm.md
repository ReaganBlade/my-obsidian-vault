## Introduction
Prim's Algorithm is a greedy algorithm used to find the **Minimum Spanning Tree (MST)** of a connected, undirected, weighted graph. An MST is a subset of edges that connects all vertices with the minimum total edge weight, without forming cycles. D
eveloped by Robert C. Prim in 1957 (though earlier described by Vojtěch Jarník in 1930), it’s particularly efficient for dense graphs and is widely used in network optimization, such as designing efficient electrical grids or communication networks.

This document covers:
1. The concept of Prim's Algorithm in the context of graphs.
2. A detailed explanation of its mechanics.
3. A Python implementation with code analysis.

---

## Graphs: The Context
A **graph** consists of:
- **Vertices (Nodes):** Entities like cities or network hubs.
- **Edges:** Connections with weights (e.g., distances, costs).
- **Undirected:** Edges are bidirectional.
- **Weighted:** Edges have numerical values.

### Minimum Spanning Tree (MST)
- **Definition:** A tree that spans all vertices with the minimum total edge weight and no cycles.
- **Properties:**
  - Contains \(V-1\) edges (where \(V\) is the number of vertices).
  - Connects all nodes.
  - Minimizes the sum of edge weights.
- **Uniqueness:** Unique if all edge weights are distinct; otherwise, multiple MSTs may exist.

### Problem Statement
Given a connected, undirected, weighted graph, find an MST that connects all vertices with the least total weight, starting from any chosen vertex.

---

## How Prim's Algorithm Works

### Core Idea
Prim's Algorithm builds the MST by:
1. Starting from an arbitrary vertex.
2. Growing the tree by repeatedly adding the smallest-weight edge that connects a vertex in the MST to a vertex outside it.
3. Using a **priority queue** (e.g., min-heap) to efficiently select the next smallest edge.

It’s a **greedy algorithm**—at each step, it picks the cheapest edge that expands the current tree without forming a cycle.

### Key Components
- **Visited Set:** Tracks vertices already in the MST.
- **Priority Queue:** Stores edges (weight, vertex) to pick the smallest next edge.
- **MST:** The growing set of edges forming the final tree.
- **Key Values:** (Optional) Tracks the minimum weight to connect each vertex to the MST.

### Step-by-Step Process
1. **Initialize:**
   - Choose a starting vertex (e.g., the first one).
   - Mark it as visited.
   - Add all its edges to a priority queue.
   - Prepare an empty MST.

2. **Grow the Tree:**
   - While the priority queue is not empty and not all vertices are visited:
     - Extract the edge with the smallest weight (weight, u, v).
     - If \(v\) is unvisited:
       - Add \(v\) to the visited set.
       - Add the edge (u, v) to the MST.
       - Add all unvisited neighbors of \(v\) to the priority queue.

3. **Stop:**
   - When all vertices are visited (MST has \(V-1\) edges).

4. **Result:**
   - The MST contains the selected edges with the minimum total weight.

### Example
Graph with 4 nodes: A, B, C, D.
- Edges: A-B (1), A-C (4), B-C (2), B-D (5), C-D (3).
- Start at A.

| Step | Current Vertex | Edge Added | Weight | Visited    | MST             |
|------|----------------|------------|--------|------------|-----------------|
| 1    | A              | A-B        | 1      | {A, B}     | {A-B}           |
| 2    | B              | B-C        | 2      | {A, B, C}  | {A-B, B-C}      |
| 3    | C              | C-D        | 3      | {A, B, C, D} | {A-B, B-C, C-D} |

**Result:** MST = {A-B (1), B-C (2), C-D (3)}, total weight = 6.

---

## Python Implementation

Here’s a Python implementation using a priority queue (via `heapq`) for efficiency.

```python
import heapq

def prim(graph, start):
    # Initialize data structures
    visited = set([start])
    mst = []
    pq = []  # Priority queue: (weight, u, v)
    total_weight = 0

    # Add all edges from the starting vertex to the priority queue
    for v, weight in graph[start].items():
        heapq.heappush(pq, (weight, start, v))

    # Process until all vertices are included
    while pq and len(visited) < len(graph):
        weight, u, v = heapq.heappop(pq)

        # Skip if v is already in MST
        if v in visited:
            continue

        # Add vertex and edge to MST
        visited.add(v)
        mst.append((u, v, weight))
        total_weight += weight

        # Add all edges from the new vertex to the priority queue
        for next_vertex, next_weight in graph[v].items():
            if next_vertex not in visited:
                heapq.heappush(pq, (next_weight, v, next_vertex))

    return mst, total_weight

# Example graph as adjacency list (node: {neighbor: weight}, undirected)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 3},
    'D': {'B': 5, 'C': 3}
}

# Run Prim's Algorithm from node 'A'
mst, total_weight = prim(graph, 'A')

# Print results
print("Minimum Spanning Tree (Edges and Weights):")
for u, v, weight in mst:
    print(f"{u} -- {v}: {weight}")
print(f"Total Weight: {total_weight}")
```

### Code Explanation
1. **Initialization:**
   - `visited`: Starts with the initial vertex.
   - `mst`: Stores the edges of the MST.
   - `pq`: Priority queue of edges (weight, u, v).
   - Add all edges from the start vertex to `pq`.

2. **Main Loop:**
   - Extract the smallest-weight edge from `pq`.
   - If the destination vertex (\(v\)) isn’t visited:
     - Add \(v\) to `visited`.
     - Add the edge to `mst`.
     - Add \(v\)’s unvisited neighbors to `pq`.

3. **Graph Representation:**
   - Adjacency list: Undirected edges are bidirectional (e.g., A-B and B-A).
   - Weights are stored with each neighbor.

4. **Output:**
   - `mst`: List of edges (u, v, weight).
   - `total_weight`: Sum of edge weights in the MST.

### Sample Output
```
Minimum Spanning Tree (Edges and Weights):
A -- B: 1
B -- C: 2
C -- D: 3
Total Weight: 6
```

---

## Time Complexity
- **O((V + E) log V)** with a binary heap:
  - \(V\): Number of vertices.
  - \(E\): Number of edges.
  - Heap operations (insert, extract-min) are O(log V).
- **O(E log V)** dominates in practice, as each edge is processed at most once.

## Space Complexity
- **O(V + E)**:
  - \(V\) for the visited set and heap.
  - \(E\) for the priority queue in the worst case.

## Advantages
- Efficient for dense graphs (many edges).
- No need to sort all edges upfront (unlike Kruskal’s).
- Works naturally with an adjacency list or matrix.

## Limitations
- Assumes the graph is connected (no MST if disconnected).
- Less intuitive for sparse graphs compared to Kruskal’s.

## Applications
- **Network Design:** Minimum-cost cabling or road networks.
- **Cluster Analysis:** Connecting points with minimal total distance.
- **Approximation Algorithms:** Solving problems like Steiner Tree.
