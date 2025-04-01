# Introduction to Graphs - Data Structure and Algorithm

## What is a Graph?

A graph is a non-linear data structure consisting of **vertices (nodes)** and **edges (links)**. It is used to represent relationships between different entities.

- **Vertices (Nodes):** The fundamental units of a graph that represent entities.
- **Edges (Links):** The connections between vertices that define relationships.
- **Graph Order:** The number of vertices in a graph.
- **Graph Size:** The number of edges in a graph.

### [[Graph Representation]]

## Types of Graphs

### Based on Direction:

1. **Directed Graph (Digraph):** Each edge has a direction, meaning it goes from one vertex to another.
2. **Undirected Graph:** Edges have no direction and can be traversed both ways.

### Based on Weights:

3. **Weighted Graph:** Edges have an associated weight (cost, distance, time, etc.).
4. **Unweighted Graph:** All edges have equal weight or no assigned weight.

### Based on Cyclic Nature:

5. **Cyclic Graph:** Contains at least one cycle, meaning there is a path that starts and ends at the same vertex.
6. **Acyclic Graph:** No cycles present in the graph.

### Based on Connectivity:

7. **Connected Graph:** There is a path between every pair of vertices.
8. **Disconnected Graph:** At least one pair of vertices is not connected.
9. **Strongly Connected Graph (for Directed Graphs):** Every vertex is reachable from every other vertex.
10. **Weakly Connected Graph:** If edges are considered as undirected, the graph becomes connected.

### Special Types of Graphs:

11. **Tree:** A connected acyclic graph.
12. **Bipartite Graph:** A graph whose vertices can be divided into two independent sets such that no two vertices within the same set are adjacent.
13. **Complete Graph:** Every vertex is connected to every other vertex.
14. **Sparse Graph:** Number of edges is much lower than the maximum possible edges.
15. **Dense Graph:** Number of edges is close to the maximum possible edges.

## [[Graph Traversal Algorithms]]

Graph traversal means visiting all the nodes of a graph in some order.

1. **Depth-First Search (DFS):**
    
    - Uses a stack (recursion or explicit stack).
    - Explores as deep as possible before backtracking.
    - Time Complexity: O(V + E).
    - Space Complexity: O(V) (for recursive call stack or explicit stack).
    - Applications:
        - Detecting cycles in a graph.
        - Solving maze problems.
        - Pathfinding algorithms.
2. **Breadth-First Search (BFS):**
    
    - Uses a queue.
    - Explores all neighbors of a node before moving to the next level.
    - Time Complexity: O(V + E).
    - Space Complexity: O(V) (for queue storage).
    - Applications:
        - Finding the shortest path in an unweighted graph.
        - Peer-to-peer networks.
        - Social network connections.

## Applications of Graphs

Graphs are widely used in various real-world applications, including:

- **Social Networks:** Representing relationships (Facebook, LinkedIn).
- **Web Crawling:** Search engines use graphs to crawl web pages.
- **Navigation Systems:** Google Maps uses graphs for shortest path algorithms.
- **Computer Networks:** Routing protocols in networks use graph theory.
- **Recommendation Systems:** Netflix, YouTube, and Amazon use graphs to recommend content.
- **Dependency Resolution:** Package managers like npm and pip use graphs to resolve dependencies.

## [[Common Graph Algorithms]]

### 1. Shortest Path Algorithms

- **Dijkstra's Algorithm:** Finds the shortest path from a source node to all other nodes in a weighted graph (non-negative weights). Time Complexity: O((V+E) log V).
- **Bellman-Ford Algorithm:** Works for graphs with negative weights but slower than Dijkstra. Time Complexity: O(VE).
- **Floyd-Warshall Algorithm:** Computes shortest paths between all pairs of nodes. Time Complexity: O(V^3).

### 2. Minimum Spanning Tree (MST) Algorithms

- **Kruskal's Algorithm:** Uses a greedy approach to find the MST by sorting edges. Time Complexity: O(E log E).
- **Prim's Algorithm:** Builds the MST by adding edges step by step. Time Complexity: O((V+E) log V).

### 3. Other Important Graph Algorithms

- **Topological Sorting:** Used for Directed Acyclic Graphs (DAGs). Time Complexity: O(V + E).
- **Tarjan's Algorithm:** Finds Strongly Connected Components (SCC) in a graph. Time Complexity: O(V + E).
- **Kosaraju’s Algorithm:** Another algorithm to find SCCs in O(V + E) time.
- **Eulerian Path and Circuit:** Used in problems related to traversing all edges exactly once.
- **Hamiltonian Path and Circuit:** Used in problems like the Traveling Salesman Problem (TSP).

## Conclusion

Graphs are a fundamental data structure with numerous applications in real-world scenarios. Understanding different types of graphs, their representations, and traversal techniques is crucial for solving complex problems efficiently. Mastering graph algorithms like DFS, BFS, Dijkstra's, Kruskal's, and Prim's provides a solid foundation for tackling computational problems in various domains.