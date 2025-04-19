# Overview of Graph Algorithms

Graphs are widely used in computer science to model relationships between objects. Graph algorithms help solve problems related to connectivity, traversal, shortest paths, and optimization.

## Types of Graph Algorithms

### 1. **Shortest Path Algorithms**

These algorithms find the shortest path between nodes in a weighted graph.

- **[[Dijkstra's Algorithm]]:** Finds the shortest path from a single source (greedy approach, O(V log V)).
- **[[Bellman-Ford Algorithm]]:** Works with negative weights but is slower (O(VE)).
- **[[Floyd-Warshall Algorithm]]:** Computes shortest paths between all pairs (O(V^3)).

### 2. **Minimum Spanning Tree (MST) Algorithms**

Finds a subset of edges forming a tree that connects all vertices with minimal cost.

- **[[Kruskal’s Algorithm]]:** Uses a greedy approach and union-find (O(E log V)).
- **[[Prim’s Algorithm]]:** Uses a priority queue for efficiency (O(V log V)).

### 3. **Topological Sorting**

Used for scheduling tasks represented as Directed Acyclic Graphs (DAGs).

- **[[Kahn’s Algorithm]] (BFS-based).**
- **[[DFS-Based Topological Sorting]]**

### 4. **Cycle Detection Algorithms**

Used to check whether a cycle exists in a graph.

- **[[DFS-Based Cycle Detection Algorithm]]** (for directed graphs).
- **[[Cycle Detection Using Union-Find Algorithm]]** (for undirected graphs).

### 5. **Network Flow Algorithms**

Used to find the maximum possible flow in a network.

- **[[Ford-Fulkerson Algorithm]]:** Uses augmenting paths (O(E * max_flow)).
- **[[Edmonds-Karp Algorithm]]:** BFS-based implementation of Ford-Fulkerson (O(VE^2)).

### 6. **Graph Coloring Algorithms**

Assigns colors to graph vertices such that no two adjacent vertices share the same color.

- Used in scheduling, register allocation, and map coloring.

## Applications of Graph Algorithms

- **Social Networks:** Finding connections, mutual friends.
- **Navigation Systems:** GPS routing (Dijkstra, A* algorithm).
- **Compiler Design:** Dependency resolution using topological sorting.
- **Networking:** Routing and load balancing.
- **Artificial Intelligence:** Search algorithms in AI and game theory.

## Conclusion

Graph algorithms form the backbone of many computer science applications. Understanding their efficiency and real-world use cases is essential for optimizing problem-solving in various domains.