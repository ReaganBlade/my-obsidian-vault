## Overview
A **Priority Queue** is a specialized queue where elements are dequeued based on their priority rather than their arrival order. It follows the **First In, First Out (FIFO)** principle but processes higher-priority elements first.

## Types of Priority Queue
1. **Min-Priority Queue**: The element with the lowest value is dequeued first.
2. **Max-Priority Queue**: The element with the highest value is dequeued first.

## Implementation in Python (Using Heap)
```python
import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item, priority):
        heapq.heappush(self.queue, (priority, item))
    
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! No elements to dequeue.")
            return None
        return heapq.heappop(self.queue)[1]
    
    def peek(self):
        return None if self.is_empty() else self.queue[0][1]
    
    def is_empty(self):
        return len(self.queue) == 0

# Example Usage
pq = PriorityQueue()
pq.enqueue("Task A", 2)
pq.enqueue("Task B", 1)
pq.enqueue("Task C", 3)
print(pq.dequeue())  # Output: Task B (highest priority, lowest number)
print(pq.peek())  # Output: Task A
```

## Applications of Priority Queue
- **Task Scheduling**: Used in operating systems to prioritize processes.
- **Dijkstra’s Algorithm**: Helps in shortest path computations.
- **Event-Driven Simulations**: Manages events occurring at different times.
- **Data Compression (Huffman Coding)**: Used in file compression algorithms.
- **Network Routing**: Manages packet scheduling based on priority.

## Advantages
- **Efficient Sorting**: Automatically arranges elements based on priority.
- **Faster Retrieval**: High-priority elements are accessed quickly.
- **Useful in Critical Applications**: Essential for real-time and high-priority task management.

## Disadvantages
- **More Overhead**: Maintaining priority order requires extra processing.
- **Complex Implementation**: Compared to simple queues, managing priorities adds complexity.
- **Fixed Priority Criteria**: Some applications may require dynamic priority adjustments.

## When to Use Priority Queue
- When processing elements based on priority rather than order.
- When implementing scheduling algorithms (CPU, task, or network).
- When working with pathfinding algorithms like Dijkstra’s.
