## 1. Introduction

Abstract Data Types (ADT) define a logical description of data and operations without specifying implementation details. They provide a high-level way to model data structures that can be implemented in different ways.

---

## 2. Characteristics of ADT

- **Encapsulation**: Hides implementation details from the user.
- **Well-defined Operations**: ADTs define operations that can be performed on data.
- **Independence**: ADTs can be implemented using different data structures.

---

## 3. Common Abstract Data Types

### 3.1 List ADT

A collection of ordered elements where duplicates are allowed.

**Operations:**

- `insert(position, element)`: Inserts an element at a specific position.
- `delete(position)`: Removes an element from a given position.
- `get(position)`: Retrieves an element at a specific position.
- `size()`: Returns the number of elements.

### 3.2 Stack ADT

A collection following Last In First Out (LIFO) order.

**Operations:**

- `push(element)`: Adds an element to the top.
- `pop()`: Removes and returns the top element.
- `peek()`: Returns the top element without removing it.
- `isEmpty()`: Checks if the stack is empty.

### 3.3 Queue ADT

A collection following First In First Out (FIFO) order.

**Operations:**

- `enqueue(element)`: Adds an element to the rear.
- `dequeue()`: Removes and returns the front element.
- `front()`: Returns the front element without removing it.
- `isEmpty()`: Checks if the queue is empty.

### 3.4 Deque (Double-Ended Queue) ADT

A queue where elements can be added or removed from both ends.

**Operations:**

- `insertFront(element)`: Inserts an element at the front.
- `insertRear(element)`: Inserts an element at the rear.
- `deleteFront()`: Removes the front element.
- `deleteRear()`: Removes the rear element.
- `isEmpty()`: Checks if the deque is empty.

### 3.5 Priority Queue ADT

A queue where elements have priority and are dequeued based on priority rather than arrival order.

**Operations:**

- `insert(element, priority)`: Adds an element with a priority.
- `remove()`: Removes and returns the element with the highest priority.
- `peek()`: Returns the highest-priority element without removing it.

### 3.6 Set ADT

A collection of unique elements with no specific order.

**Operations:**

- `insert(element)`: Adds an element if it does not exist.
- `remove(element)`: Removes an element.
- `contains(element)`: Checks if an element is present.
- `size()`: Returns the number of elements.

### 3.7 Map (Dictionary) ADT

A collection of key-value pairs where each key is unique.

**Operations:**

- `put(key, value)`: Inserts or updates a key-value pair.
- `get(key)`: Retrieves the value associated with a key.
- `remove(key)`: Deletes a key-value pair.
- `containsKey(key)`: Checks if a key exists.
- `size()`: Returns the number of key-value pairs.

---

## 4. Implementation of ADTs

ADTs can be implemented using various data structures:

|ADT|Common Implementations|
|---|---|
|List|Array, Linked List|
|Stack|Array, Linked List|
|Queue|Array, Linked List|
|Deque|Doubly Linked List|
|Priority Queue|Heap|
|Set|Hash Table, BST|
|Map|Hash Table, BST|

---

## 5. Importance of ADTs

- **Code Reusability**: ADTs provide modular components that can be reused.
- **Abstraction**: ADTs separate the implementation from the user.
- **Efficiency**: Choosing the right ADT can optimize performance.
- **Scalability**: ADTs provide a structured approach to data management.

---

## 6. Conclusion

Abstract Data Types (ADT) are a fundamental concept in data structures and programming. They provide a way to model and manipulate data efficiently without focusing on low-level implementation details.

---

## 7. References

- Introduction to Algorithms - Cormen et al.
- Data Structures and Algorithm Analysis - Mark Allen Weiss