## Overview
A **dynamic stack** is implemented using a linked list, allowing it to grow and shrink dynamically without a predefined size. Unlike a static stack, it does not suffer from **stack overflow** as long as memory is available. It follows the **Last In, First Out (LIFO)** principle.

## Implementation in Python
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DynamicStack:
    def __init__(self):
        self.top = None  # Represents an empty stack

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack Underflow! No elements to pop.")
            return None
        item = self.top.data
        self.top = self.top.next
        return item

    def peek(self):
        return None if self.top is None else self.top.data

    def is_empty(self):
        return self.top is None

# Example Usage
stack = DynamicStack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())  # Output: 30
print(stack.peek())  # Output: 20
```

## Applications of Dynamic Stack
- **Recursion Handling**: Used in function call stacks to support recursion.
- **Expression Parsing**: Used in evaluating postfix, prefix, and infix expressions.
- **Undo/Redo Functionality**: Used in text editors and other applications.
- **Web Browsing History**: Helps in implementing back/forward navigation in browsers.
- **Graph Traversal**: Used in Depth-First Search (DFS) algorithm.

## Advantages
- **No Fixed Size**: Can grow and shrink dynamically based on needs.
- **Efficient Memory Usage**: Uses only the memory required for active elements.
- **No Stack Overflow**: Unlike static stacks, it does not have a predefined limit.

## Disadvantages
- **Extra Memory Overhead**: Each element requires additional memory for pointer storage.
- **Slower than Static Stack**: Pointer manipulation introduces extra computational overhead.
- **More Complex Implementation**: Requires linked list management compared to an array.

## When to Use Dynamic Stack
- When dealing with an unknown or varying number of elements.
- When implementing recursive algorithms that require a function call stack.
- When handling operations where memory efficiency is crucial.
