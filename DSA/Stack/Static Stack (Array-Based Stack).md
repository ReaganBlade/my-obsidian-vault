## Overview
A **static stack** is implemented using an array with a fixed size. It follows the **Last In, First Out (LIFO)** principle, meaning the last inserted element is the first to be removed. Since it has a fixed size, memory allocation is predefined, which can lead to **stack overflow** if the stack exceeds its limit.

## Implementation in Python
```python
class StaticStack:
    def __init__(self, capacity):
        self.stack = [None] * capacity  # Fixed-size array
        self.capacity = capacity
        self.top = -1  # Represents an empty stack

    def push(self, item):
        if self.top >= self.capacity - 1:
            print("Stack Overflow! Cannot push more elements.")
            return
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.top == -1:
            print("Stack Underflow! No elements to pop.")
            return None
        item = self.stack[self.top]
        self.stack[self.top] = None  # Optional: Clear the slot
        self.top -= 1
        return item

    def peek(self):
        return None if self.top == -1 else self.stack[self.top]

    def is_empty(self):
        return self.top == -1

# Example Usage
stack = StaticStack(3)
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())  # Output: 30
print(stack.peek())  # Output: 20
```

## Applications of Static Stack
- **Expression Evaluation**: Used in parsing mathematical expressions.
- **Function Call Stack**: Used in programming languages to manage function calls.
- **Undo/Redo Operations**: Helps in implementing undo/redo features in applications.
- **Backtracking Algorithms**: Used in maze-solving, DFS, and recursive algorithms.
- **Memory Management**: Used in compilers for managing execution stacks.

## Advantages
- **Fast Operations**: Push and pop operations take O(1) time.
- **Memory Efficient**: Predefined memory allocation avoids fragmentation.
- **Simple to Implement**: Uses an array, making it easy to understand and use.

## Disadvantages
- **Fixed Size**: Cannot grow beyond its predefined limit, leading to overflow.
- **Wasted Memory**: If the stack is not fully utilized, unused space is wasted.
- **Lack of Flexibility**: Cannot dynamically resize, making it less adaptable to changing data sizes.

## When to Use Static Stack
- When the maximum number of elements is known in advance.
- When memory allocation must be controlled strictly.
- When performance is a priority and resizing overhead should be avoided.
