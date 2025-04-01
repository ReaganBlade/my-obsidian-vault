## Introduction

Breadth-First Search (BFS) is a fundamental graph traversal algorithm used to explore nodes layer by layer. It is widely used in pathfinding, connectivity problems, and AI search techniques.

## How BFS Works

BFS starts from a source node and explores all its neighbors before moving on to the next level. It follows a **FIFO (First-In-First-Out) order**, utilizing a queue to track nodes.

### Steps:

1. Start from a given node (source node).
2. Enqueue the node and mark it as visited.
3. Dequeue a node, process it, and enqueue all its unvisited adjacent nodes.
4. Repeat until the queue is empty.

## BFS Implementation in Python

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])

# Example Graph Representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')
```

## Time and Space Complexity

- **Time Complexity:** O(V + E), where V = vertices and E = edges.
- **Space Complexity:** O(V), as it stores all vertices in the queue.

## Applications of BFS

- **Shortest Path in Unweighted Graphs** (e.g., social networks, maze solving)
- **Web Crawlers** (indexing web pages layer by layer)
- **Network Broadcasting** (sending signals to all nodes)
- **AI & Game Trees** (solving puzzles and finding the best move)

## Advantages of BFS

- Guarantees finding the shortest path in unweighted graphs.
- Works efficiently in small to moderately large graphs.

## Disadvantages of BFS

- High memory usage for storing nodes in the queue.
- Not suitable for deep graphs (DFS is more space-efficient).

## Conclusion

BFS is a powerful algorithm for graph traversal, particularly useful in applications requiring level-wise exploration. Choosing BFS over DFS depends on the problem constraints and memory considerations.