jjjjjhn h  1. Trivial Graph
	1. A graph (G = (v, e)) is said to be trivial if there only exists one single vertex in the graph without any edge.
	2. aka Singleton graph or single vertex graph.
	3. Simplest type of graph often used as starting point for building more complex graphs.
2. Finite Graph
	1. A graph with finite number of Vertex and Edges are called Finite Graph.
	2. Used to represent real-world situations.
3. Infinite Graph
	1. A graph with infinite number of Vertex and Edges.
	2. Extend indifinitely.
4. Simple Graph
	1. A graph with no Loops and no Parallel Edges is called a Simple Graph.
5. Cycle Graph
	1. A simple graph with 'n' vertices (n >= 3) and 'n' edges is called a cycle graph if all its edges form a cycle of length 'n'. If the degree of each vetex in the graph is two. Denoted by **Cn**.
6. Complete Graph
	1. All vertex is connected to all the other vertex
	2. Formuala to calculate number of edges in a complete graph
		1. kn = n(n-1)/2
		2. where n = # of vertices
7. Null Graph
	1. Modified Version of a Trivial Graph. A graph G = (V, E) is said to a null graph if there are n number of vertices exist, but no Edge exists that connects then. This is the same as ordering food from a different city or farther places.

Isolated Vertex -> vertex that are connected to no other vertex and neither have a self loop.

Note:
vertex with self loop will always have 2 edges.


**Directed Graph**
- In-degree: the count of incoming edges
- Out-degree: the count of outgoing edges

If a vertex have a self loop and an out going edge then the self loop will be counted as incoming edge (degree 1)


NOTE: 
What is a vertex that has no outgoing edges

Graph Representation:
### Adjacency Matrix
### Incidence Matrix
normally v -> v
but in incidence, v -> e

used to represent weighted Graph
outgoing edges -> 1
incoming edges -> -1

the table is created as v -> e


|     | e1  | e2  | e3  | e4  |
| --- | --- | --- | --- | --- |
| a   | 0   | 1   | -1  | 0   |
| b   | 1   | 0   | -1  |     |
| c   |     |     |     |     |

### Linked list representation
- null 
- 

Dense Graph
- Max possible edges
- max suited for adjacency matrix
- 

Sparse Graph
- Graph with minimum number of edges

Symmetric matrix is formed when you have an undirected graph


Use of Null Graph:
- A "null graph" (also called an empty graph or edgeless graph) is a graph with no vertices or edges, and its primary use is ==as a foundational concept in graph theory, serving as a basis for understanding more complex graph structures and properties==.


### Spanning Tree
A spanning tree is ==a subset of a graph that connects all its vertices using the fewest possible edges.== A spanning tree has no cycles or loops.

Undirected connected graph

Edges -> no of vertices  - 1
note: we cannot create a spanning tree of a weighted graph.


Properties:
- can have more than one spanning tree
- must not contain any cycle
- given graph is a cycle graph, then the number of possible spanning trees will be equal to the number of vertices of the given graph
- if complete graph, then the number of possible spanning trees can be calculated using Cayley's Formula -> (n + 1) ^ (n - 1) | v ^ v - 2
- spanning tree cannot be disconnected. If you remove any edge from the created tree then it won't be considered as a spanning tree anymore

### MINIMUM SPANNING TREE (MST)
- MST can stand for ==Mountain Standard Time, Minimum Spanning Tree, Multi-Skill Technician, or Minimum Standard of Treatment==.


 
April 7th, 2025
### Finding Shortest Path Methods
1. Single Source Shortest Path
	1. Dijkstra's (Can be used but might generate Incorrect result), Relaxes Only Once
		1. Relaxation
		2. Formula for Relaxtion
	2. Bellman Ford (Can also work for Negative Weight)
		1. Relaxation -> (v - 1) times
		2. Negative Weight Cycle
2. All pair Shortest Path
	1. Floyd Warshall Algorithm (Can also work for Negative Weight)


G -> M = 50
M -> E = 30

### NOTE: Negative Weight Cycle
if the distance is updated at vth iteration, then Negative Weight Cycle is present in the graph

Edge Relaxation -> updating with latest minim distance


Date: April 08, 2025

Approaches for Algorithm

1. Greedy
2. Comparison
3. Divide and Conquer
4. Dynamic Prog

### Floyd Warshall Algorithm

uses dynammic programming approach
Works in dense graph
finds shortest path of all pairs

Conditions:
1. Graph must be weighted
2. No Negative Weight Cycle
3. Better for Dense Graph

Graph Rep: Adjacency Matrix




### Step-by-Step Process
1. **Initialize:**
   - Create a distance matrix:
     - \(`dist[i][j]` = weight(i, j)\) if an edge exists.
     - \(`dist[i][j]` = infinity) if no edge (unless (i = j), then 0).
   - Optionally, initialize a predecessor matrix with direct connections.

2. **Iterate Over Intermediate Vertices:**
   - For each vertex \(k\) (from 0 to \(V-1\)):
     - For each pair \((i, j)\):
       - If  (`dist[i][k]` + `dist[k][j]` < `dist[i][j]`), update (`dist[i][j]`) and set (`pred[i][j]` = `pred[k][j]`).

3. **Negative Cycle Check:**
   - After completion, check the diagonal (`dist[i][i]`).
   - If any \(`dist[i][i]` < 0\), a negative cycle exists.

4. **Result:**
   - The final distance matrix contains shortest path lengths between all pairs.
   - The predecessor matrix (if used) allows path reconstruction.


Number of Matrix -> v + 1


Date: April 22, 2025 -> Monday
## Graph Traversal

Two Types of traversal:
1. [[Breadth First Search]] (BFS) Traversal -> Queue
2. Depth First Search (DFS) Traversal -> Stack