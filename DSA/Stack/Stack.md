# Stack Data Structure Overview

## Introduction
A **stack** is a linear data structure that follows the **Last In, First Out (LIFO)** principle, meaning the last element added is the first one to be removed. It is widely used in computing for various applications such as expression evaluation, memory management, and function calls.

## Types of Stacks
1. [[Static Stack (Array-Based Stack)]] - Implemented using an array with a fixed size.
2. [[Dynamic Stack (Linked List-Based Stack)]]- Implemented using a linked list, allowing dynamic memory allocation.
3. [[Double-Ended Stack (Deque-Based Stack)]] - Supports insertion and deletion from both ends.

## Basic Operations
- **Push:** Insert an element onto the stack.
- **Pop:** Remove the top element from the stack.
- **Peek (Top):** Retrieve the top element without removing it.
- **isEmpty:** Check if the stack is empty.
- **isFull:** Check if the stack is full (in case of a static stack).

## Applications of Stacks
- **Function Call Management:** Used in recursion and function calls (Call Stack).
- **Expression Evaluation:** Used in evaluating postfix and prefix expressions.
- **Undo/Redo Operations:** Implemented in text editors and applications.
- **Browser Back/Forward Navigation:** Maintains history of visited pages.
- **Parenthesis Matching:** Used in syntax parsing.

## Limitations of Stacks
- **Limited Size:** In static stacks, the size is fixed, leading to possible overflow.
- **Memory Usage:** Dynamic stacks require extra memory for pointer storage.
- **Sequential Access:** Elements can only be accessed in LIFO order.

## Conclusion
Stacks are an essential data structure with diverse applications in computing. Understanding their behavior and limitations is crucial for efficient algorithm design and software development.
