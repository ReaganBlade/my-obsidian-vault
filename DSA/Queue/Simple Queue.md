## Overview
A **simple queue** is the most basic form of a queue that follows the **First In, First Out (FIFO)** principle. Elements are added at the rear (enqueue) and removed from the front (dequeue).

## Implementation in Python
```python
class SimpleQueue:
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
queue = SimpleQueue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.dequeue())  # Output: 10
print(queue.peek())  # Output: 20
```

## Applications of Simple Queue
- **Job Scheduling**: Managing tasks in an orderly fashion.
- **Process Management**: Used in operating systems for handling processes.
- **Data Buffering**: Storing and managing data packets in networks.
- **Printer Spooling**: Managing print jobs in a sequential manner.

## Advantages
- **Maintains Order**: Ensures elements are processed in the same order they arrive.
- **Simple and Efficient**: Easy to implement with minimal complexity.

## Disadvantages
- **Shifting Overhead**: Removing elements requires shifting the remaining elements.
- **Limited Direct Access**: Unlike arrays, elements cannot be accessed randomly.

## When to Use Simple Queue
- When elements need to be processed in order.
- When implementing basic scheduling or buffering mechanisms.
- When managing sequential tasks such as request handling.