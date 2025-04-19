## Introduction

The **Ford-Fulkerson algorithm** is a method used to compute the **maximum flow** in a flow network. It is based on finding augmenting paths in a residual graph and increasing the flow along these paths until no more augmenting paths exist.

## Key Concepts

- **Flow Network**: A directed graph where each edge has a capacity and a flow.
    
- **Source (s)**: The starting node where the flow originates.
    
- **Sink (t)**: The ending node where the flow is collected.
    
- **Residual Graph**: A graph representing the remaining capacities of edges after accounting for the current flow.
    
- **Augmenting Path**: A path from the source to the sink where additional flow can be pushed.
    

## Algorithm Steps

1. Start with an initial flow of 0.
    
2. Construct the residual graph based on available capacities.
    
3. Find an augmenting path using Depth-First Search (DFS) or Breadth-First Search (BFS).
    
4. Determine the minimum capacity (bottleneck) along the augmenting path.
    
5. Update the residual graph by subtracting the bottleneck flow from forward edges and adding it to reverse edges.
    
6. Repeat until no more augmenting paths exist.
    
7. The sum of flow values leaving the source is the maximum flow.
    

## Python Implementation

```python
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = defaultdict(lambda: defaultdict(int))  # Adjacency list representation
    
    def add_edge(self, u, v, capacity):
        """Adds an edge with given capacity to the graph."""
        self.graph[u][v] = capacity
    
    def bfs(self, source, sink, parent):
        """Performs BFS to find an augmenting path."""
        visited = set()
        queue = [source]
        visited.add(source)
        
        while queue:
            u = queue.pop(0)
            for v, capacity in self.graph[u].items():
                if v not in visited and capacity > 0:  # Unvisited node with available capacity
                    queue.append(v)
                    visited.add(v)
                    parent[v] = u
                    if v == sink:
                        return True
        return False
    
    def ford_fulkerson(self, source, sink):
        """Computes the maximum flow using the Ford-Fulkerson method."""
        parent = {}  # Stores path information
        max_flow = 0
        
        while self.bfs(source, sink, parent):
            # Find the maximum flow through the path found by BFS
            path_flow = float('Inf')
            v = sink
            while v != source:
                u = parent[v]
                path_flow = min(path_flow, self.graph[u][v])
                v = parent[v]
            
            # Update residual capacities in the graph
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow  # Reverse flow
                v = parent[v]
            
            max_flow += path_flow
        
        return max_flow

# Example Usage
graph = Graph(6)
graph.add_edge(0, 1, 16)
graph.add_edge(0, 2, 13)
graph.add_edge(1, 2, 10)
graph.add_edge(1, 3, 12)
graph.add_edge(2, 1, 4)
graph.add_edge(2, 4, 14)
graph.add_edge(3, 2, 9)
graph.add_edge(3, 5, 20)
graph.add_edge(4, 3, 7)
graph.add_edge(4, 5, 4)

source, sink = 0, 5
print("The maximum possible flow is", graph.ford_fulkerson(source, sink))
```

## Explanation of the Code

1. **Graph Representation**: We use a dictionary of dictionaries to store the adjacency list.
    
2. **Adding Edges**: The `add_edge` function stores the capacity of edges.
    
3. **Finding an Augmenting Path**: BFS is used to find a path from the source to the sink.
    
4. **Updating Residual Graph**: After finding the path, we update capacities to reflect the flow.
    
5. **Computing Maximum Flow**: We iterate until no augmenting path exists and sum the flow values.
    

## Complexity Analysis

- BFS runs in **O(V + E)** time.
    
- Each augmenting path is found in **O(E)** time.
    
- The algorithm runs in **O(E * max_flow)** in the worst case.
    

## Applications

- Network routing and optimization.
    
- Bipartite matching.
    
- Project selection and job scheduling.
    
- Image segmentation in computer vision.
    

## Conclusion

The **Ford-Fulkerson algorithm** is an intuitive and effective method to find the maximum flow in a network. It utilizes augmenting paths and residual graphs to iteratively push flow until the network is saturated. The Python implementation efficiently demonstrates this approach.