A graph can be represented in several ways, depending on the use case and efficiency requirements. The common representations include:

1. **Adjacency Matrix**
    
    - A 2D array where `matrix[i][j] = 1` (or weight in weighted graphs) if there is an edge between vertices `i` and `j`, otherwise `0`.
        
    - **Space Complexity**: O(V2)O(V^2)
        
    - **Best For**: Dense graphs.
        
2. **Adjacency List**
    
    - A list where each index represents a vertex, and stores a list of its adjacent vertices.
        
    - **Space Complexity**: O(V+E)O(V + E)
        
    - **Best For**: Sparse graphs.
        
3. **Edge List**
    
    - A list of pairs (or triplets for weighted graphs) representing edges, e.g., `[(u, v), (v, w), ...]`.
        
    - **Space Complexity**: O(E)O(E)
        
    - **Best For**: Edge-centric operations.
        
4. **Incidence Matrix**
    
    - A 2D matrix where rows represent vertices and columns represent edges; `matrix[i][j] = 1` if vertex `i` is incident to edge `j`.
        
    - **Space Complexity**: O(VE)O(VE)
        
    - **Best For**: Graphs with a small number of edges relative to vertices.
        

Each representation has its trade-offs in terms of space and time complexity. Let me know if you need details on a specific one! 🚀