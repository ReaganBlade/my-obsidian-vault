## Introduction

A **Binary Tree** is a hierarchical data structure where each node has at most **two children**. It is widely used in computer science for searching, sorting, and hierarchical data storage.

## Properties of a Binary Tree

1. Each node has at most **two children**: a left child and a right child.
2. The topmost node is called the **root**.
3. Each node contains a **value (data)** and pointers to left and right children.
4. The last level of the tree may not be completely filled.
5. **Depth**: The number of edges from the root to a node.
6. **Height**: The number of edges from a node to the deepest leaf.

## Types of Binary Trees

1. **Full Binary Tree** - Every node has **0 or 2 children**.
2. **Complete Binary Tree** - All levels are completely filled except possibly the last.
3. **Perfect Binary Tree** - All levels are completely filled.
4. **Balanced Binary Tree** - The height difference between left and right subtrees is at most **1**.
5. **Degenerate (Skewed) Binary Tree** - Each node has only one child.

## Structure of a Binary Tree Node

A typical node contains:

- **Data**: The value stored in the node.
- **Left Pointer**: Pointer to the left child.
- **Right Pointer**: Pointer to the right child.

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
```

## Operations on Binary Tree

### 1. **Insertion Operation**

Inserting a node in a binary tree is done based on the tree type. In a **Binary Search Tree (BST)**, it follows:

- If the key is smaller than the root, insert in the left subtree.
- If the key is larger than the root, insert in the right subtree.

```python
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root
```

### 2. **Search Operation**

Search follows the BST property.

```python
def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)
```

### 3. **Traversal Methods**

1. **Inorder (Left → Root → Right)**

```python
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)
```

2. **Preorder (Root → Left → Right)**

```python
def preorder(root):
    if root:
        print(root.key, end=' ')
        preorder(root.left)
        preorder(root.right)
```

3. **Postorder (Left → Right → Root)**

```python
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=' ')
```

4. **Level Order Traversal (Breadth-First Search)**

```python
from collections import deque

def level_order(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.key, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

### 4. **Deletion Operation**

Deleting a node involves three cases:

- Node has **no children**: Simply delete it.
- Node has **one child**: Replace node with its child.
- Node has **two children**: Replace with the **inorder successor**.

```python
def delete(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current
```

## Time Complexity

|Operation|Average Case|Worst Case|
|---|---|---|
|Search|O(log n)|O(n)|
|Insert|O(log n)|O(n)|
|Delete|O(log n)|O(n)|

## Applications of Binary Trees

1. **Expression Trees** – Used in compilers for parsing expressions.
2. **File Systems** – Organizing hierarchical data structures.
3. **Databases** – B-Trees and Binary Search Trees are used for indexing.
4. **Artificial Intelligence** – Decision Trees are a type of binary tree.

## Conclusion

- Binary Trees are fundamental data structures with hierarchical relationships.
- They enable efficient searching, sorting, and retrieval operations.
- Understanding tree traversal and manipulation is crucial for **coding interviews**.