## Introduction
The DFS-based Cycle Detection Algorithm uses **Depth-First Search (DFS)** to determine whether a graph contains a cycle. A cycle is a path that starts and ends at the same vertex, forming a closed loop. This algorithm is versatile, working on both directed and undirected graphs, with slight variations in logic depending on the graph type. It’s widely used in applications like deadlock detection, dependency analysis, and validating prerequisites (e.g., ensuring a DAG for topological sorting).

This document covers:
1. The concept of cycle detection using DFS in the context of graphs.
2. A detailed explanation of its mechanics for directed and undirected graphs.
3. A Python implementation with code analysis for both cases.

---

## Graphs: The Context
A **graph** consists of:
- **Vertices (Nodes):** Entities like tasks, cities, or processes.
- **Edges:** Connections between vertices, which may be:
  - **Directed:** One-way (e.g., \(u \to v\)).
  - **Undirected:** Two-way (e.g., \(u - v\)).
- **Cycle:** A sequence of edges forming a loop (e.g., \(A \to B \to C \to A\)).

### Cycle Detection
- **Directed Graphs:** A cycle exists if a vertex is revisited within the same DFS path (back edge to an ancestor in the recursion stack).
- **Undirected Graphs:** A cycle exists if a visited vertex is encountered again, excluding the immediate parent (since undirected edges are bidirectional).
- **Goal:** Identify if such a loop exists, which impacts algorithms like topological sorting (requires DAGs) or MST construction (requires no cycles).

### Problem Statement
Given a graph (directed or undirected), determine if it contains a cycle using DFS.

---

## How DFS-Based Cycle Detection Works

### Core Idea
DFS explores the graph by traversing as deep as possible along each branch before backtracking. During this process:
- For **directed graphs**, it tracks vertices in the current recursion stack to detect back edges (indicating a cycle).
- For **undirected graphs**, it checks for revisits to already visited vertices, excluding the parent, to detect cycles.

The algorithm uses DFS’s recursive nature to systematically explore paths and identify loops.

### Key Components
- **Visited Set:** Tracks vertices that have been fully explored.
- **Recursion Stack (Directed):** Tracks vertices in the現在の DFS path to detect back edges.
- **Parent Tracking (Undirected):** Avoids false positives in bidirectional edges.
- **Cycle Flag:** Indicates if a cycle is found.

### Step-by-Step Process

#### Directed Graphs
1. **Initialize:**
   - Create a visited set and a recursion stack (temp set).
   - Start DFS from each unvisited vertex.

2. **DFS Traversal:**
   - Mark the current vertex as in the recursion stack.
   - Explore all unvisited neighbors:
     - If a neighbor is in the recursion stack, a cycle is detected (back edge).
     - Recursively apply DFS to unvisited neighbors.
   - Remove the vertex from the recursion stack and mark it visited.

3. **Result:**
   - If a cycle is detected, return True; otherwise, False.

#### Undirected Graphs
1. **Initialize:**
   - Create a visited set.
   - Start DFS from each unvisited vertex with a parent parameter (initially None).

2. **DFS Traversal:**
   - Mark the current vertex as visited.
   - Explore all neighbors:
     - If a neighbor is visited and not the parent, a cycle is detected.
     - Recursively apply DFS to unvisited neighbors, passing the current vertex as the parent.

3. **Result:**
   - If a cycle is detected, return True; otherwise, False.

### Example

#### Directed Graph
- Nodes: 0, 1, 2, 3.
- Edges: 0→1, 1→2, 2→0, 2→3.

| Step | Vertex | Stack    | Visited | Cycle? |
|------|--------|----------|---------|--------|
| 0    | 0      | [0]      | {}      | No     |
| 1    | 1      | [0, 1]   | {}      | No     |
| 2    | 2      | [0, 1, 2]| {}      | No     |
| 3    | 0 (in stack) | [0, 1, 2] | {}   | Yes    |

**Result:** Cycle detected (0→1→2→0).

#### Undirected Graph
- Nodes: A, B, C.
- Edges: A-B, B-C, C-A.

| Step | Vertex | Parent | Visited | Cycle? |
|------|--------|--------|---------|--------|
| 0    | A      | None   | {A}     | No     |
| 1    | B      | A      | {A, B}  | No     |
| 2    | C      | B      | {A, B, C} | Yes (C-A, A ≠ B) |

**Result:** Cycle detected (A-B-C-A).

---

## Python Implementation

Here’s a Python implementation for both directed and undirected graphs using DFS.

```python
from collections import defaultdict

# Directed Graph Cycle Detection
def has_cycle_directed(graph, vertices):
    visited = set()
    rec_stack = set()

    def dfs(vertex):
        visited.add(vertex)
        rec_stack.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True  # Cycle detected

        rec_stack.remove(vertex)
        return False

    for vertex in vertices:
        if vertex not in visited:
            if dfs(vertex):
                return True
    return False

# Undirected Graph Cycle Detection
def has_cycle_undirected(graph, vertices):
    visited = set()

    def dfs(vertex, parent):
        visited.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                if dfs(neighbor, vertex):
                    return True
            elif neighbor != parent:
                return True  # Cycle detected

        return False

    for vertex in vertices:
        if vertex not in visited:
            if dfs(vertex, None):
                return True
    return False

# Example graphs
# Directed Graph (with cycle)
directed_graph = {
    '0': ['1'],
    '1': ['2'],
    '2': ['0', '3'],
    '3': []
}
directed_vertices = ['0', '1', '2', '3']

# Undirected Graph (with cycle)
undirected_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}
undirected_vertices = ['A', 'B', 'C']

# Test the algorithms
print("Directed Graph has cycle:", has_cycle_directed(directed_graph, directed_vertices))
print("Undirected Graph has cycle:", has_cycle_undirected(undirected_graph, undirected_vertices))
```

### Code Explanation

#### Directed Graph
1. **Initialization:**
   - `visited`: Tracks fully processed vertices.
   - `rec_stack`: Tracks vertices in the current DFS path.

2. **DFS Function:**
   - Adds the vertex to both `visited` and `rec_stack`.
   - Recursively explores neighbors:
     - If unvisited, continue DFS.
     - If in `rec_stack`, a cycle is found.
   - Removes the vertex from `rec_stack` on backtracking.

3. **Main Loop:**
   - Ensures all components are checked.

#### Undirected Graph
1. **Initialization:**
   - `visited`: Tracks processed vertices.
   - `parent`: Tracks the previous vertex to avoid false positives.

2. **DFS Function:**
   - Marks the vertex as visited.
   - Explores neighbors:
     - If unvisited, recurse with the current vertex as parent.
     - If visited and not the parent, a cycle is found.

3. **Main Loop:**
   - Handles disconnected components with an initial null parent.

#### Graph Representation
- Adjacency list: `graph[u]` lists neighbors.
- Directed: Edges are one-way.
- Undirected: Edges are bidirectional (explicitly listed both ways).

### Sample Output
```
Directed Graph has cycle: True
Undirected Graph has cycle: True
```

---

## Time Complexity
- **O(V + E)**:
  - \(V\): Number of vertices.
  - \(E\): Number of edges.
  - Each vertex and edge is visited once during DFS.

## Space Complexity
- **O(V)**:
  - \(V\) for the recursion stack, visited set, and (in directed case) recursion stack set.

## Advantages
- Linear time complexity, efficient for sparse and dense graphs.
- Naturally detects cycles during traversal.
- Works for both directed and undirected graphs with minor adjustments.

## Limitations
- Recursive implementation may hit stack limits for very large graphs (mitigated with an iterative DFS).
- Requires careful handling of undirected edges to avoid false positives.

## Applications
- **Deadlock Detection:** Identifying circular waits in resource allocation.
- **Dependency Validation:** Ensuring no cyclic dependencies in software or tasks.
- **Graph Analysis:** Validating DAGs for topological sorting.
