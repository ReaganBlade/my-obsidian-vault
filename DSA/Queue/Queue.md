## Overview
A **queue** is a linear data structure that follows the **First In, First Out (FIFO)** principle. This means that the first element added to the queue is the first one to be removed, similar to a real-world queue (e.g., a line at a ticket counter).

## Types of Queue
1. [[Simple Queue]]: Basic FIFO queue.
2. [[Circular Queue]]: The last position is connected back to the first, making it circular.
3. [[Priority Queue]]: Elements are dequeued based on priority rather than order.
4. [[Double-Ended Queue (Deque)]]: Allows insertion and deletion from both ends.

## Implementation in Python
```python
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! No elements to dequeue.")
            return None
        return self.queue.pop(0)
    
    def peek(self):
        return None if self.is_empty() else self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0

# Example Usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
print(queue.dequeue())  # Output: 10
print(queue.peek())  # Output: 20
```

## Applications of Queue
- **Task Scheduling**: Used in CPU and disk scheduling algorithms.
- **Print Queue**: Manages print jobs in an orderly fashion.
- **Breadth-First Search (BFS)**: Used in graph and tree traversal.
- **Data Buffering**: Used in streaming applications for handling data flow.
- **Message Queues**: Used in messaging systems to handle multiple requests.

## Advantages
- **Efficient Processing**: Ensures order in task execution.
- **Flexible Variants**: Supports different types like circular, priority, and double-ended queues.
- **Useful in Real-World Scenarios**: Mimics real-world processing like job scheduling and networking.

## Disadvantages
- **Limited Direct Access**: Unlike arrays, elements cannot be accessed randomly.
- **Shifting Overhead**: In simple queues using arrays, dequeuing requires shifting elements.
- **Memory Usage**: Depending on the type of queue, extra memory may be needed for pointers.

## When to Use Queue
- When processing elements in the order they arrive.
- When implementing scheduling or buffering mechanisms.
- When performing BFS or other sequential operations.
