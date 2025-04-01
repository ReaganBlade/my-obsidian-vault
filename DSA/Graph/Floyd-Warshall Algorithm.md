## Introduction
The Floyd-Warshall Algorithm is a dynamic programming approach to find the **shortest paths between all pairs of vertices** in a weighted graph. Unlike Dijkstra’s (single-source, non-negative weights) or Bellman-Ford (single-source, negative weights), Floyd-Warshall computes shortest paths for **every pair of nodes** in one run. It handles both positive and negative edge weights and can detect negative cycles, making it versatile for applications like network analysis or transit systems.

This document covers:
1. The concept of Floyd-Warshall in the context of graphs.
2. A detailed explanation of its mechanics.
3. A Python implementation with code analysis.

---

## Graphs: The Context
A **graph** consists of:
- **Vertices (Nodes):** Entities like cities, routers, or points.
- **Edges:** Connections with weights (e.g., distances, costs), which can be positive or negative.
- **Directed/Undirected:** Floyd-Warshall works with both, though undirected graphs are typically converted to directed by duplicating edges.

### Key Differences
- **All-Pairs vs. Single-Source:** Unlike Dijkstra’s or Bellman-Ford, it solves for all pairs (e.g., shortest path from A to B, A to C, B to D, etc.).
- **Negative Weights:** Handles them, like Bellman-Ford, but for all pairs.
- **Matrix-Based:** Uses an adjacency matrix, unlike the adjacency list common in other algorithms.

### Problem Statement
Given a weighted graph, compute the shortest path between every pair of vertices, even with negative weights, and identify negative cycles if present.

---

## How Floyd-Warshall Works

### Core Idea
Floyd-Warshall builds a **distance matrix** that evolves from direct edge weights to shortest path lengths by considering intermediate vertices. It uses dynamic programming with the principle: “If there’s a shorter path from \(i\) to \(j\) through an intermediate vertex \(k\), update the distance.” It systematically checks all possible intermediate nodes.

### Key Components
- **Distance Matrix:** Tracks shortest distances between all pairs (\(dist[i][j]\)).
- **Predecessor Matrix:** (Optional) Tracks the path for reconstruction.
- **Relaxation:** Updates distances by testing all vertices as intermediaries.

### Step-by-Step Process
1. **Initialize:**
   - Create a distance matrix:
     - \(dist[i][j] = weight(i, j)\) if an edge exists.
     - \(dist[i][j] = \infty\) if no edge (unless \(i = j\), then 0).
   - Optionally, initialize a predecessor matrix with direct connections.

2. **Iterate Over Intermediate Vertices:**
   - For each vertex \(k\) (from 0 to \(V-1\)):
     - For each pair \((i, j)\):
       - If \(dist[i][k] + dist[k][j] < dist[i][j]\), update \(dist[i][j]\) and set \(pred[i][j] = pred[k][j]\).

3. **Negative Cycle Check:**
   - After completion, check the diagonal (\(dist[i][i]\)).
   - If any \(dist[i][i] < 0\), a negative cycle exists.

4. **Result:**
   - The final distance matrix contains shortest path lengths between all pairs.
   - The predecessor matrix (if used) allows path reconstruction.

### Example
Graph with 4 nodes: 0, 1, 2, 3.
- Edges: 0→1 (4), 0→2 (8), 1→2 (2), 1→3 (5), 2→1 (-3).

**Initial Distance Matrix:**
```
   0   1   2   3
0 [0,  4,  8,  ∞]
1 [∞,  0,  2,  5]
2 [∞, -3,  0,  ∞]
3 [∞,  ∞,  ∞,  0]
```

**After \(k=0\):**
- No change (0 as intermediate doesn’t improve paths yet).

**After \(k=1\):**
```
   0   1   2   3
0 [0,  4,  6,  9]
1 [∞,  0,  2,  5]
2 [∞, -3,  0,  ∞]
3 [∞,  ∞,  ∞,  0]
```
- 0→1→2 = 6 < 8, 0→1→3 = 9 < ∞.

**After \(k=2\):**
```
   0   1   2   3
0 [0,  3,  6,  9]
1 [∞,  0,  2,  5]
2 [∞, -3,  0,  ∞]
3 [∞,  ∞,  ∞,  0]
```
- 0→2→1 = 3 < 4.

**After \(k=3\):**
- No change.

**Negative Cycle Check:**
- \(dist[1][1] = 0\), but 1→2→1 = -1 < 0 (cycle via edges), indicating a negative cycle.

**Result:** Shortest distances computed, but a negative cycle exists.

---

## Python Implementation

Here’s a Python implementation that computes all-pairs shortest paths and detects negative cycles.

```python
def floyd_warshall(graph, vertices):
    # Number of vertices
    V = len(vertices)
    
    # Initialize distance and predecessor matrices
    dist = [[float('infinity')] * V for _ in range(V)]
    pred = [[None] * V for _ in range(V)]
    
    # Fill initial distances and predecessors
    for i in range(V):
        dist[i][i] = 0  # Distance to self is 0
        for j, weight in graph[vertices[i]].items():
            j_idx = vertices.index(j)
            dist[i][j_idx] = weight
            pred[i][j_idx] = i  # Direct predecessor

    # Floyd-Warshall algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] != float('infinity') and dist[k][j] != float('infinity'):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        pred[i][j] = pred[k][j]

    # Check for negative cycles
    for i in range(V):
        if dist[i][i] < 0:
            return dist, pred, True  # Negative cycle detected

    return dist, pred, False

# Example graph as adjacency list (node: {neighbor: weight})
graph = {
    '0': {'1': 4, '2': 8},
    '1': {'2': 2, '3': 5},
    '2': {'1': -3},
    '3': {}
}
vertices = ['0', '1', '2', '3']

# Run Floyd-Warshall
dist, pred, has_negative_cycle = floyd_warshall(graph, vertices)

# Print results
if has_negative_cycle:
    print("Graph contains a negative cycle. Shortest paths may be undefined.")
else:
    print("Shortest distances between all pairs:")
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            print(f"{vertices[i]} to {vertices[j]}: {dist[i][j]}")

    # Reconstruct path (example: 0 to 3)
    def get_path(pred, vertices, start, end):
        start_idx = vertices.index(start)
        end_idx = vertices.index(end)
        if dist[start_idx][end_idx] == float('infinity'):
            return "No path"
        path = []
        current = end_idx
        while current is not None:
            path.append(vertices[current])
            current = pred[start_idx][current]
            if current == start_idx:
                path.append(vertices[start_idx])
                break
        return path[::-1]  # Reverse path

    print("Path from 0 to 3:", get_path(pred, vertices, '0', '3'))
```

### Code Explanation
1. **Initialization:**
   - `dist`: \(V \times V\) matrix, infinity everywhere except diagonal (0).
   - `pred`: Tracks predecessors, initially set for direct edges.
   - Populate `dist` and `pred` from the graph’s adjacency list.

2. **Main Loop:**
   - Triple nested loop: \(k\) (intermediate), \(i\) (source), \(j\) (destination).
   - Update \(dist[i][j]\) if going through \(k\) is shorter.
   - Update \(pred[i][j]\) to reflect the new path.

3. **Negative Cycle Detection:**
   - Check diagonal elements (\(dist[i][i]\)).
   - If any are negative, a cycle exists (e.g., a node can reach itself cheaper than 0).

4. **Graph Representation:**
   - Adjacency list: Converted to a matrix for processing.
   - Nodes are strings, mapped to indices via `vertices`.

5. **Output:**
   - If no negative cycle: `dist` and `pred` for all pairs.
   - If negative cycle: Warns that distances may be unreliable.

### Sample Output
```
Graph contains a negative cycle. Shortest paths may be undefined.
```

---

## Time Complexity
- **O(V³)**:
  - \(V\): Number of vertices.
  - Three nested loops, each iterating \(V\) times.

## Space Complexity
- **O(V²)**: For the `dist` and `pred` matrices.

## Advantages
- Computes all-pairs shortest paths in one run.
- Handles negative weights.
- Simple to implement with a matrix.

## Limitations
- Slower than repeated Dijkstra’s (\(O(V (V + E) log V)\)) for sparse graphs with non-negative weights.
- Requires \(O(V²)\) space, less efficient for large, sparse graphs.

## Applications
- **Transit Networks:** All-pairs distances in road or flight networks.
- **Social Networks:** Shortest influence paths between all users.
- **Cycle Detection:** Identifying negative cycles in financial or scheduling systems.
