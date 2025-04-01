## Introduction

A **Heap** is a special tree-based data structure that satisfies the **heap property**, meaning that the parent node is always greater (in Max Heap) or smaller (in Min Heap) than its children. Heaps are commonly implemented using **binary heaps**, which are complete binary trees stored in arrays for efficient access.

## Properties of a Heap

1. **Complete Binary Tree**: All levels are completely filled except possibly the last level, which is filled from left to right.
2. **Heap Property**:
    - **Max Heap**: The parent node is always **greater than or equal to** its children.
    - **Min Heap**: The parent node is always **smaller than or equal to** its children.
3. **Efficient Operations**: Heaps allow **O(log n) insertion and deletion** and **O(1) access** to the root element.

## Structure of a Heap Node

Heaps are usually implemented using arrays. Given a node at index **i**:

- **Left child** is at `2 * i + 1`
- **Right child** is at `2 * i + 2`
- **Parent** is at `(i - 1) // 2`

## Implementation of a Min Heap

```python
class MinHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)
    
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_value
    
    def _heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)
```

## Operations on Heap

### 1. **Insertion** (O(log n))

- Insert the new element at the end.
- Perform **heapify-up** to maintain the heap property.

### 2. **Deletion (Extract Min/Max)** (O(log n))

- Replace the root with the last element.
- Perform **heapify-down** to restore the heap property.

### 3. **Peek (Get Min/Max)** (O(1))

- The minimum or maximum element is always at the root (index 0).

## Applications of Heap

1. **Priority Queue**: Used in scheduling and process management.
2. **Heap Sort**: Efficient sorting algorithm with O(n log n) complexity.
3. **Graph Algorithms**: Used in Dijkstra’s and Prim’s algorithms.
4. **Median Finding**: Helps maintain the median in a dynamic dataset.

## Time Complexity

|Operation|Complexity|
|---|---|
|Insert|O(log n)|
|Delete|O(log n)|
|Peek|O(1)|
|Heap Sort|O(n log n)|

## Conclusion

- **Heaps provide efficient priority-based access** to elements.
- **Used extensively in algorithms** that require priority management.
- **Binary Heaps are the most commonly used heap structure** in computer science.