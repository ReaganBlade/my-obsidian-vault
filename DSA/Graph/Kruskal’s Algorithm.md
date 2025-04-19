## Introduction
Kruskal's Algorithm is a greedy algorithm used to find the **Minimum Spanning Tree (MST)** of a connected, undirected, weighted graph. An MST is a subset of edges that connects all vertices with the minimum total edge weight, without forming any cycles. Proposed by Joseph Kruskal in 1956, it’s widely used in network design (e.g., laying cables or roads) to minimize costs.

This document covers:
1. The concept of Kruskal's Algorithm in the context of graphs.
2. A detailed explanation of its mechanics.
3. A Python implementation with code analysis.

---

## Graphs: The Context
A **graph** consists of:
- **Vertices (Nodes):** Entities like cities or junctions.
- **Edges:** Connections with weights (e.g., distances, costs).
- **Undirected:** Edges have no direction (bidirectional connections).
- **Weighted:** Edges have numerical values.

### Minimum Spanning Tree (MST)
- **Definition:** A tree (no cycles) that spans all vertices with the minimum total edge weight.
- **Properties:**
  - Contains \(V-1\) edges (where \(V\) is the number of vertices).
  - Connects all nodes (spanning).
  - Minimizes the sum of edge weights.
- **Uniqueness:** An MST is unique if all edge weights are distinct; otherwise, multiple MSTs may exist.

### Problem Statement
Given a connected, undirected, weighted graph, find an MST that connects all vertices with the least total weight.

---

## How Kruskal's Algorithm Works

### Core Idea
Kruskal's Algorithm builds the MST by:
1. Sorting all edges by weight (smallest first).
2. Adding edges to the MST one by one, ensuring no cycles are formed.
3. Using a **disjoint-set (union-find)** data structure to efficiently detect cycles.

It’s a **greedy algorithm**—at each step, it picks the smallest edge that doesn’t violate the MST properties.

### Key Components
- **Edge List:** A list of all edges with their weights.
- **Disjoint-Set Data Structure:** Tracks which vertices belong to the same connected component (to avoid cycles).
- **MST:** The growing set of edges forming the final tree.

### Step-by-Step Process
1. **Initialize:**
   - Sort all edges in non-decreasing order of weight.
   - Create a disjoint-set for each vertex (each starts as its own component).
   - Prepare an empty MST.

2. **Process Edges:**
   - For each edge (u, v, weight) in sorted order:
     - Check if \(u\) and \(v\) are in different components (using `find`).
     - If they are, add the edge to the MST and merge their components (using `union`).
     - If they’re in the same component, skip (adding it would form a cycle).

3. **Stop:**
   - When the MST has \(V-1\) edges or all edges are processed.

4. **Result:**
   - The MST contains the selected edges with the minimum total weight.

### Example
Graph with 4 nodes: A, B, C, D.
- Edges: A-B (1), A-C (4), B-C (2), B-D (5), C-D (3).

| Step | Edge | Weight | Action         | MST             |
|------|------|--------|----------------|-----------------|
| 1    | A-B  | 1      | Add            | {A-B}           |
| 2    | B-C  | 2      | Add            | {A-B, B-C}      |
| 3    | C-D  | 3      | Add            | {A-B, B-C, C-D} |
| 4    | A-C  | 4      | Skip (cycle)   | {A-B, B-C, C-D} |
| 5    | B-D  | 5      | Skip (enough)  | {A-B, B-C, C-D} |

**Result:** MST = {A-B (1), B-C (2), C-D (3)}, total weight = 6.

---

## Python Implementation

Here’s a Python implementation using a disjoint-set data structure for efficiency.

```python
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        # Find the root of the set with path compression
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, set1, set2):
        # Union by rank to keep tree balanced
        root1 = self.find(set1)
        root2 = self.find(set2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal(graph, vertices):
    # Convert graph to edge list: (weight, u, v)
    edges = []
    for u in graph:
        for v, weight in graph[u].items():
            if (v, u) not in [(x[1], x[2]) for x in edges]:  # Avoid duplicates in undirected graph
                edges.append((weight, u, v))
    
    # Sort edges by weight
    edges.sort()

    # Initialize disjoint-set and MST
    ds = DisjointSet(vertices)
    mst = []

    # Process edges
    for weight, u, v in edges:
        if ds.find(u) != ds.find(v):  # If no cycle
            ds.union(u, v)
            mst.append((u, v, weight))

    return mst

# Example graph as adjacency list (node: {neighbor: weight}, undirected)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 3},
    'D': {'B': 5, 'C': 3}
}
vertices = ['A', 'B', 'C', 'D']

# Run Kruskal's Algorithm
mst = kruskal(graph, vertices)

# Print results
print("Minimum Spanning Tree (Edges and Weights):")
total_weight = 0
for u, v, weight in mst:
    print(f"{u} -- {v}: {weight}")
    total_weight += weight
print(f"Total Weight: {total_weight}")
```

### Code Explanation
1. **DisjointSet Class:**
   - `find`: Returns the root of a vertex’s set with path compression for efficiency.
   - `union`: Merges two sets by rank to minimize tree height.
   - Initializes each vertex as its own set.

2. **Kruskal Function:**
   - Converts the adjacency list to an edge list (weight, u, v).
   - Sorts edges by weight.
   - Uses DisjointSet to check for cycles and build the MST.

3. **Graph Representation:**
   - Adjacency list: Undirected edges are bidirectional (e.g., A-B and B-A).
   - Edge list avoids duplicates by checking pairs.

4. **Output:**
   - MST as a list of edges (u, v, weight).
   - Total weight calculated for verification.

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
- **O(E log E) or O(E log V)**:
  - \(E\): Number of edges (sorting dominates).
  - \(V\): Number of vertices.
  - Union-find operations are nearly O(1) with path compression and rank.
- Sorting \(E\) edges: O(E log E).
- Union-find for \(E\) edges: O(E α(V)), where α is the inverse Ackermann function (effectively constant).

## Space Complexity
- **O(V + E)**:
  - \(V\) for the disjoint-set.
  - \(E\) for the edge list.

## Advantages
- Simple and intuitive.
- Works well for sparse graphs (fewer edges).
- Easily implemented with a good disjoint-set structure.

## Limitations
- Requires sorting, which can be slow for dense graphs (use Prim’s for dense graphs).
- Assumes the graph is connected (no MST if disconnected).

## Applications
- **Network Design:** Minimum-cost wiring or piping.
- **Clustering:** Building hierarchical structures.
- **Approximation Algorithms:** Solving problems like the Traveling Salesman Problem.
