## Introduction

A **stack** is a linear data structure that follows the **Last In, First Out (LIFO)** principle, meaning the last element added to the stack is the first one to be removed. The concept of the stack was introduced by **Friedrich L. Bauer** in the 1950s as part of his work on computer programming and data structures.

	## What is a Stack?
	
	A stack is an abstract data type (ADT) with two primary operations:
	
	- **Push**: Adds an element to the top of the stack.
	- **Pop**: Removes the top element from the stack.

### Key Properties:

- Follows LIFO (Last In, First Out) principle.
- Can be implemented using arrays or linked lists.
- Used in recursion, expression evaluation, backtracking, etc.

## Stack Operations

The fundamental operations performed on a stack are:

1. **Push(x)**: Adds an element `x` to the top of the stack.
2. **Pop()**: Removes and returns the top element of the stack.
3. **Peek() or Top()**: Returns the top element without removing it.
4. **isEmpty()**: Checks if the stack is empty.
5. **Size()**: Returns the number of elements in the stack.

## Advantages of Stack

- **Efficient**: Operations like push and pop take constant time **O(1)**.
- **Easy to implement**: Simple and intuitive data structure.
- **Used in various applications** like recursion, expression evaluation, undo/redo operations, etc.

## Disadvantages of Stack

- **Limited access**: Can only access the top element.
- **Fixed size (in arrays)**: If implemented using an array, resizing is required when full.
- **Not efficient for searching**: Traversal is not straightforward compared to other data structures like linked lists.

## Implementation of Stack in Python

### Using List (Built-in)

```python
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
```

### Using Collections (Deque)

Python's `collections.deque` is a better alternative since it provides O(1) time complexity for push and pop operations.

```python
from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return "Stack is empty"
    
    def peek(self):
        if self.stack:
            return self.stack[-1]
        return "Stack is empty"
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
```

### Using Queue Module (LifoQueue)

Python’s `queue.LifoQueue` is another way to implement a stack.

```python
from queue import LifoQueue

stack = LifoQueue(maxsize=5)  # Create a stack with a max size of 5
stack.put(1)  # Push operation
stack.put(2)
print(stack.get())  # Pop operation
```

## Stack in Python Standard Library (STL)

Python provides a built-in stack implementation via:

6. **List** (with `append()` and `pop()`).
7. **Deque from collections** (optimized for stack operations).
8. **LifoQueue from queue module** (thread-safe but has overhead).

### Methods in Python's STL for Stack

|Method|List|Deque|LifoQueue|
|---|---|---|---|
|Push|`append(x)`|`append(x)`|`put(x)`|
|Pop|`pop()`|`pop()`|`get()`|
|Peek|`stack[-1]`|`stack[-1]`|No direct method|
|isEmpty|`len(stack) == 0`|`len(stack) == 0`|`stack.empty()`|

## Applications of Stack

- **Function call management (Recursion)**. -> Tower of Hanoi Problem
- **Undo/Redo operations in editors**.
- **Expression evaluation (Infix to Postfix, Prefix conversion)**.
- **Backtracking (Maze solving, N-Queens Problem)**. -> 
- **Web browser history (Back and Forward navigation)**.
- **Memory Management** 
- **Polish Notations**
- **Symbol** - Paranthesis Balance 

## Conclusion

Stack is a simple yet powerful data structure widely used in programming. Python provides multiple ways to implement stacks, with `collections.deque` being the most efficient option. Understanding stack operations and applications is crucial for problem-solving and algorithm design.