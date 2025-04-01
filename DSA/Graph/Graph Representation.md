# Graph Representations

Graphs can be represented in multiple ways depending on the requirements of the problem, memory constraints, and the type of graph (dense or sparse). The two most common representations are the **Adjacency Matrix** and the **Adjacency List**.

## 1. [[Adjacency Matrix]]

An **Adjacency Matrix** is a 2D array (or matrix) of size `V x V`, where `V` is the number of vertices in the graph. It is useful for dense graphs where the number of edges is close to the maximum possible.

### Characteristics:

- Each row and column represent a vertex in the graph.
- The value `matrix[i][j]` is `1` (or the edge weight in weighted graphs) if there is an edge from vertex `i` to vertex `j`, otherwise it is `0`.
- For an **undirected graph**, the matrix is symmetric, meaning `matrix[i][j] = matrix[j][i]`.
- For a **directed graph**, `matrix[i][j] = 1` does not imply `matrix[j][i] = 1`.

### Space Complexity:

- **O(V^2)**, regardless of the number of edges.
- Not memory efficient for **sparse graphs** (graphs with fewer edges).

### Pros:

- Constant-time (O(1)) edge lookup.
- Simpler to implement and understand.
- Efficient for dense graphs where `E ≈ V^2`.

### Cons:

- Requires more space for sparse graphs.
- Inserting or deleting an edge takes O(1) time, but finding all adjacent vertices takes O(V) time.

---

## 2. [[Adjacency List]]

An **Adjacency List** is a collection of lists, maps, or dictionaries where each vertex stores a list of its adjacent vertices. This representation is more memory-efficient for sparse graphs.

### Characteristics:

- Each vertex has a list of connected vertices.
- The list can be implemented using arrays, linked lists, or hashmaps.
- In a **weighted graph**, each edge stores an additional value representing the weight.

### Space Complexity:

- **O(V + E)**, where `V` is the number of vertices and `E` is the number of edges.
- More efficient than an adjacency matrix for **sparse graphs**.

### Pros:

- Space-efficient for large graphs with fewer edges.
- Faster edge iteration; finding all adjacent nodes takes **O(degree of vertex)** rather than **O(V)**.
- Dynamic: adding and removing edges is faster compared to an adjacency matrix.

### Cons:

- Checking if an edge exists between two vertices takes **O(V)** in the worst case.
- Slightly more complex to implement compared to an adjacency matrix.

---

## Comparison of Graph Representations

|Feature|Adjacency List|Adjacency Matrix|
|---|---|---|
|Space Complexity|O(V + E)|O(V^2)|
|Edge Lookup|O(V)|O(1)|
|Adding an Edge|O(1)|O(1)|
|Removing an Edge|O(V)|O(1)|
|Finding Neighbors|O(degree of V)|O(V)|
|Best for|Sparse Graphs|Dense Graphs|

---

## Conclusion

Both adjacency lists and adjacency matrices have their advantages and disadvantages. The choice between them depends on the problem constraints:

- **Use an adjacency matrix** when dealing with dense graphs, where quick edge lookups are needed.
- **Use an adjacency list** for sparse graphs, where memory efficiency is a priority and edge iteration is common.

These representations form the foundation for graph algorithms like BFS, DFS, Dijkstra’s algorithm, and more.