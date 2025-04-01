## Introduction

Depth-First Search (DFS) is a fundamental graph traversal algorithm that explores as far as possible along each branch before backtracking. It is widely used in pathfinding, cycle detection, and topological sorting.

## How DFS Works

DFS follows a **LIFO (Last-In-First-Out) order**, typically implemented using recursion or a stack.

### Steps:

1. Start from a given node (source node).
2. Mark it as visited.
3. Explore all unvisited adjacent nodes recursively (or using a stack).
4. Backtrack when no more adjacent nodes are available.

## DFS Implementation in Python (Recursive Approach)

```python
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

# Example Graph Representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs_recursive(graph, 'A')
```

## DFS Implementation in Python (Iterative Approach)

```python
from collections import deque

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            stack.extend(graph[node][::-1])  # Reverse to maintain order

# Running the DFS Iterative function
dfs_iterative(graph, 'A')
```

## Time and Space Complexity

- **Time Complexity:** O(V + E), where V = vertices and E = edges.
- **Space Complexity:**
    - O(V) for recursive DFS (stack calls for deep graphs).
    - O(V) for iterative DFS (explicit stack storage).

## Applications of DFS

- **Cycle Detection in Graphs** (detecting circular dependencies)
- **Topological Sorting** (ordering tasks with dependencies)
- **Solving Mazes and Puzzles** (navigating backtracking problems)
- **Connected Components in Graphs** (detecting isolated clusters)
- **Artificial Intelligence** (search problems, decision trees)

## Advantages of DFS

- Uses less memory compared to BFS for deep graphs.
- Works well for problems requiring exhaustive search (e.g., backtracking).

## Disadvantages of DFS

- May get stuck in infinite loops in cyclic graphs if not handled properly.
- Does not guarantee the shortest path in unweighted graphs (BFS does).

## Conclusion

DFS is an essential algorithm for graph traversal, particularly useful when deep exploration is needed. Understanding when to use DFS over BFS depends on the problem's constraints and the graph's structure.