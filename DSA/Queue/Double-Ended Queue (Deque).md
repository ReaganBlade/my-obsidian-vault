## Overview
A **Double-Ended Queue (Deque)** is a specialized queue where elements can be inserted and removed from both ends. Unlike a simple queue, which follows the **First In, First Out (FIFO)** principle, a deque provides more flexibility.

## Types of Deque
1. **Input-Restricted Deque**: Insertion allowed at one end, but deletion allowed from both ends.
2. **Output-Restricted Deque**: Deletion allowed at one end, but insertion allowed from both ends.

## Implementation in Python (Using Collections Deque)
```python
from collections import deque

class DoubleEndedQueue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue_front(self, item):
        self.queue.appendleft(item)
    
    def enqueue_rear(self, item):
        self.queue.append(item)
    
    def dequeue_front(self):
        if self.is_empty():
            print("Queue Underflow! No elements to dequeue from front.")
            return None
        return self.queue.popleft()
    
    def dequeue_rear(self):
        if self.is_empty():
            print("Queue Underflow! No elements to dequeue from rear.")
            return None
        return self.queue.pop()
    
    def peek_front(self):
        return None if self.is_empty() else self.queue[0]
    
    def peek_rear(self):
        return None if self.is_empty() else self.queue[-1]
    
    def is_empty(self):
        return len(self.queue) == 0

# Example Usage
dq = DoubleEndedQueue()
dq.enqueue_front(10)
dq.enqueue_rear(20)
print(dq.dequeue_front())  # Output: 10
print(dq.dequeue_rear())  # Output: 20
```

## Applications of Double-Ended Queue
- **Job Scheduling**: Helps in managing dynamic task prioritization.
- **Sliding Window Problems**: Used in efficient algorithms like finding max/min in a window.
- **Undo/Redo Operations**: Supports bidirectional access in applications like text editors.
- **Deque-Based Stacks & Queues**: Can simulate stack and queue functionalities efficiently.
- **Graph Algorithms**: Used in BFS (Breadth-First Search) for optimized traversal.

## Advantages
- **Flexibility**: Can function as both a queue and a stack.
- **Efficient Operations**: Supports O(1) insertions and deletions at both ends.
- **Better Performance in Certain Use Cases**: Ideal for problems requiring bidirectional access.

## Disadvantages
- **Higher Complexity**: More complicated than simple queues.
- **Memory Usage**: Might use extra space depending on the implementation.
- **Not Always Needed**: In many cases, a simple queue or stack is sufficient.

## When to Use Double-Ended Queue
- When elements need to be processed from both ends dynamically.
- When implementing undo/redo features.
- When optimizing sliding window algorithms or real-time scheduling.
