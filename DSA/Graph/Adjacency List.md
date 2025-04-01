An **adjacency list** is a common way to represent graphs in data structures and algorithms. It efficiently captures the relationships between vertices (nodes) in a graph by listing each vertex alongside its adjacent vertices.

## Definition

An adjacency list represents a graph as a collection where each vertex has a list of its adjacent vertices. This structure is particularly space-efficient for sparse graphs, where the number of edges is much less than the maximum possible number of edges.

## Representation

### Undirected Graph

In an undirected graph, each edge is bidirectional. Therefore, if vertex A is connected to vertex B, both A's and B's adjacency lists will include each other.

**Example:**

```
A -- B
|    |
C -- D
```

The adjacency list representation:

```
A: B, C
B: A, D
C: A, D
D: B, C
```

### Directed Graph

In a directed graph, edges have a direction. If there's an edge from vertex A to vertex B, only A's list will include B.

**Example:**

```
A → B
↓
C → D
```

The adjacency list representation:

```
A: B, C
B:
C: D
D:
```

### Weighted Graph

For weighted graphs, each edge has an associated weight. The adjacency list includes these weights alongside the adjacent vertices.

**Example:**

```
A --(2)-- B
|        |
(3)     (4)
|        |
C --(5)-- D
```

The adjacency list representation:

```
A: (B, 2), (C, 3)
B: (A, 2), (D, 4)
C: (A, 3), (D, 5)
D: (B, 4), (C, 5)
```

## Advantages

- **Space Efficiency:** Suitable for sparse graphs, as it doesn't allocate space for non-existent edges.
- **Edge Listing:** Quickly retrieves all edges adjacent to a vertex.

## Disadvantages

- **Edge Existence Check:** Determining if an edge exists between two vertices can be slower compared to other representations like adjacency matrices.

## Implementation in Python

```python
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # Remove for directed graphs
    
    def display(self):
        for vertex in self.graph:
            print(vertex, "->", self.graph[vertex])

# Example Usage
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.display()
```

### Output:

```
A -> ['B', 'C']
B -> ['A', 'D']
C -> ['A', 'D']
D -> ['B', 'C']
```

## Comparison with Adjacency Matrix

|Feature|Adjacency List|Adjacency Matrix|
|---|---|---|
|Space Complexity|O(V + E)|O(V^2)|
|Adding Edge|O(1)|O(1)|
|Removing Edge|O(E)|O(1)|
|Checking Edge Existence|O(E)|O(1)|
|Ideal for|Sparse Graphs|Dense Graphs|

## References

- [GeeksforGeeks: Adjacency List](https://www.geeksforgeeks.org/adjacency-list-meaning-definition-in-dsa/)