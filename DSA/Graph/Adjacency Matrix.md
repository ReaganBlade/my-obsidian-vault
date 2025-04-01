## Introduction

The **Adjacency Matrix** is a way to represent a graph using a 2D array. It is particularly useful for dense graphs where the number of edges is close to the maximum possible.

## Definition

An **Adjacency Matrix** is a square matrix of size `V x V` (where `V` is the number of vertices in the graph). Each cell `(i, j)` in the matrix represents the presence (or absence) of an edge between vertex `i` and vertex `j`.

## Properties

- **Size:** `V x V`
- **Value:** `matrix[i][j] = 1` if an edge exists, otherwise `0`
- **Space Complexity:** `O(V^2)`
- **Best for:** Dense graphs
- **Not efficient for:** Sparse graphs (wastes memory for unused edges)

## Types of Adjacency Matrices

### 1. Undirected and Unweighted Graph

- The matrix is **symmetric** (`matrix[i][j] = matrix[j][i]`).

#### **Example Graph**

```
   0 --- 1
   |     |
   2 --- 3
```

#### **Adjacency Matrix**

```
   0  1  2  3
0  0  1  1  0
1  1  0  0  1
2  1  0  0  1
3  0  1  1  0
```

#### **Python Code**

```python
V = 4
adj_matrix = [[0] * V for _ in range(V)]

def add_edge(u, v):
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1  # Because it's an undirected graph

add_edge(0, 1)
add_edge(0, 2)
add_edge(1, 3)
add_edge(2, 3)

for row in adj_matrix:
    print(row)
```

### 2. Directed and Unweighted Graph

- The matrix is **not symmetric** (`matrix[i][j] ≠ matrix[j][i]`).

#### **Example Graph**

```
   0 → 1
   ↓    ↓
   2 → 3
```

#### **Adjacency Matrix**

```
   0  1  2  3
0  0  1  1  0
1  0  0  0  1
2  0  0  0  1
3  0  0  0  0
```

#### **Python Code**

```python
V = 4
adj_matrix = [[0] * V for _ in range(V)]

def add_edge(u, v):
    adj_matrix[u][v] = 1  # Only one direction (u → v)

add_edge(0, 1)
add_edge(0, 2)
add_edge(1, 3)
add_edge(2, 3)

for row in adj_matrix:
    print(row)
```

### 3. Weighted Graph

- Instead of `1` and `0`, edges have **weights** representing cost, distance, etc.
- `matrix[i][j] = weight of edge (i → j)`

#### **Example Graph**

```
   (4)  0 → 1
    |   ↓   |
   2 → 3 ← 5
```

#### **Adjacency Matrix**

```
   0  1  2  3
0  0  4  2  0
1  0  0  0  5
2  0  0  0  3
3  0  0  0  0
```

#### **Python Code**

```python
V = 4
adj_matrix = [[0] * V for _ in range(V)]

def add_edge(u, v, weight):
    adj_matrix[u][v] = weight  # Assigning weights

add_edge(0, 1, 4)
add_edge(0, 2, 2)
add_edge(1, 3, 5)
add_edge(2, 3, 3)

for row in adj_matrix:
    print(row)
```

## Advantages and Disadvantages

### ✅ Advantages

- Easy to implement and understand.
- Checking if an edge exists is **O(1)**.
- Best for dense graphs where `E ≈ V^2`.

### ❌ Disadvantages

- Requires **O(V²)** space even if the graph is sparse.
- Adding/removing an edge takes **O(1)**, but finding all neighbors takes **O(V)**.
- Inefficient for large sparse graphs.

## Conclusion

The adjacency matrix is a powerful way to represent graphs when memory is not a constraint, and edge lookups need to be very fast. However, for graphs with a large number of vertices but few edges, adjacency lists are a more efficient alternative.