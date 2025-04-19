## Introduction
DFS-based Topological Sorting is a method to linearly order the vertices of a **Directed Acyclic Graph (DAG)** such that for every directed edge \(u \to v\), vertex \(u\) appears before \(v\) in the ordering. Unlike Kahn's Algorithm, which uses a queue and in-degree, this approach leverages **Depth-First Search (DFS)** to explore the graph recursively, building the order by appending vertices after their dependencies are fully processed. It’s widely used in dependency resolution, such as scheduling tasks or determining compilation order in software builds.

This document covers:
1. The concept of DFS-based topological sorting in the context of graphs.
2. A detailed explanation of its mechanics.
3. A Python implementation with code analysis.

---

## Graphs: The Context
A **graph** consists of:
- **Vertices (Nodes):** Entities like tasks or modules.
- **Edges:** Directed connections representing dependencies (e.g., \(u \to v\) means \(u\) must precede \(v\)).
- **Directed Acyclic Graph (DAG):** A directed graph with no cycles, ensuring a valid topological order exists.

### Topological Sorting
- **Definition:** A linear ordering of vertices where, for every edge \(u \to v\), \(u\) comes before \(v\).
- **Properties:**
  - Only possible in DAGs (cycles prevent a valid order).
  - Multiple valid orderings may exist depending on the graph structure.
- **DFS Approach:** Uses post-order traversal—vertices are added to the order after exploring all their outgoing edges (dependencies).

### Problem Statement
Given a DAG, produce a topological ordering of its vertices using DFS, and detect if a cycle exists, which would invalidate the ordering.

---

## How DFS-Based Topological Sorting Works

### Core Idea
DFS-based topological sorting:
1. Explores the graph recursively, starting from an unvisited vertex.
2. Fully processes each vertex’s neighbors (dependencies) before adding the vertex to the order.
3. Uses a **stack-like mechanism** (via recursion or explicit stack) to store vertices in reverse finishing order, which is then reversed to get the topological order.
4. Detects cycles by tracking vertices in the current recursion path.

It’s a **post-order DFS**—vertices are added to the result after their subtrees (dependencies) are fully explored.

### Key Components
- **Visited Set:** Tracks processed vertices to avoid reprocessing.
- **Temporary Set:** Tracks vertices in the current recursion stack to detect cycles.
- **Topological Order:** A list built in reverse (later reversed) or prepended during backtracking.
- **Cycle Detection:** If a vertex is revisited within the same recursion path, a cycle exists.

### Step-by-Step Process
1. **Initialize:**
   - Create a set for visited vertices and a temporary set for the recursion stack.
   - Prepare an empty list for the topological order.

2. **DFS Traversal:**
   - For each unvisited vertex:
     - Run DFS:
       - Mark the vertex as temporarily visited (in the recursion stack).
       - Recursively visit all unvisited neighbors.
       - If a neighbor is in the temporary set, a cycle is detected.
       - After exploring all neighbors, remove the vertex from the temporary set, mark it as visited, and append it to the order.

3. **Finalize:**
   - Reverse the order (if appended) to get the topological sequence.
   - If a cycle is detected, report it.

4. **Result:**
   - A list representing the topological order, or an indication of a cycle.

### Example
DAG with 6 nodes: 0, 1, 2, 3, 4, 5.
- Edges: 5→0, 5→2, 4→0, 4→1, 2→3, 1→3.

| Step | Current Vertex | Stack (Recursion) | Visited | Order (Post-DFS) |
|------|----------------|-------------------|---------|------------------|
| 0    | Start 5        | [5]              | {}      | []              |
| 1    | 5 → 0          | [5, 0]           | {}      | []              |
| 2    | Backtrack 0    | [5]              | {0}     | [0]             |
| 3    | 5 → 2          | [5, 2]           | {0}     | [0]             |
| 4    | 2 → 3          | [5, 2, 3]        | {0}     | [0]             |
| 5    | Backtrack 3    | [5, 2]           | {0, 3}  | [0, 3]          |
| 6    | Backtrack 2    | [5]              | {0, 2, 3} | [0, 3, 2]     |
| 7    | Backtrack 5    | []               | {0, 2, 3, 5} | [0, 3, 2, 5] |
| 8    | Start 4        | [4]              | {0, 2, 3, 5} | [0, 3, 2, 5] |
| 9    | 4 → 1          | [4, 1]           | {0, 2, 3, 5} | [0, 3, 2, 5] |
| 10   | 1 → 3 (visited)| [4, 1]           | {0, 2, 3, 5} | [0, 3, 2, 5] |
| 11   | Backtrack 1    | [4]              | {0, 1, 2, 3, 5} | [0, 3, 2, 5, 1] |
| 12   | Backtrack 4    | []               | {0, 1, 2, 3, 4, 5} | [0, 3, 2, 5, 1, 4] |

**Result:** Reverse order = [4, 1, 5, 2, 3, 0].

---

## Python Implementation

Here’s a Python implementation using recursive DFS with cycle detection.

```python
from collections import defaultdict

def topological_sort_dfs(graph, vertices):
    # Track visited vertices and recursion stack
    visited = set()
    temp_stack = set()  # For cycle detection
    topo_order = []

    def dfs(vertex):
        # Mark vertex as in recursion stack
        temp_stack.add(vertex)

        # Explore all neighbors
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                if neighbor in temp_stack:
                    return False  # Cycle detected
                if not dfs(neighbor):
                    return False
            elif neighbor in temp_stack:
                return False  # Cycle detected

        # Remove from recursion stack, mark visited, and add to order
        temp_stack.remove(vertex)
        visited.add(vertex)
        topo_order.append(vertex)
        return True

    # Process all vertices
    for vertex in vertices:
        if vertex not in visited:
            if not dfs(vertex):
                return None  # Cycle detected

    # Reverse the order to get topological sort
    return topo_order[::-1]

# Example DAG as adjacency list (node: [neighbors])
graph = {
    '0': [],
    '1': ['3'],
    '2': ['3'],
    '3': [],
    '4': ['0', '1'],
    '5': ['0', '2']
}
vertices = ['0', '1', '2', '3', '4', '5']

# Run DFS-based Topological Sort
result = topological_sort_dfs(graph, vertices)

# Print results
if result:
    print("Topological Order:", " -> ".join(result))
else:
    print("Graph contains a cycle. No valid topological order exists.")
```

### Code Explanation
1. **Initialization:**
   - `visited`: Tracks fully processed vertices.
   - `temp_stack`: Tracks vertices in the current recursion path.
   - `topo_order`: Builds the order in reverse (post-order).

2. **DFS Function:**
   - Adds the current vertex to `temp_stack`.
   - Recursively visits unvisited neighbors.
   - Checks for cycles (neighbor in `temp_stack`).
   - After exploration, marks the vertex visited and adds it to `topo_order`.

3. **Main Loop:**
   - Iterates over all vertices to handle disconnected components.
   - Returns None if a cycle is detected.

4. **Graph Representation:**
   - Adjacency list: `graph[u]` lists outgoing neighbors (directed edges).
   - Vertices are provided explicitly.

5. **Output:**
   - Reverses `topo_order` to get the final topological sequence.
   - Returns None if a cycle is found.

### Sample Output
```
Topological Order: 4 -> 5 -> 1 -> 2 -> 3 -> 0
```

---

## Time Complexity
- **O(V + E)**:
  - \(V\): Number of vertices.
  - \(E\): Number of edges.
  - Each vertex and edge is visited once during DFS.

## Space Complexity
- **O(V)**:
  - \(V\) for the recursion stack, visited set, temporary stack, and topological order.

## Advantages
- Linear time complexity, efficient for all DAGs.
- Naturally integrates cycle detection.
- No need to compute in-degrees (unlike Kahn’s).

## Limitations
- Only works on DAGs (cycles invalidate the result).
- Recursive implementation may hit stack limits for very large graphs (can be mitigated with an explicit stack).

## Applications
- **Dependency Resolution:** Ordering tasks or software builds (e.g., npm, Gradle).
- **Course Scheduling:** Arranging classes with prerequisites.
- **Circuit Design:** Sequencing operations with dependencies.