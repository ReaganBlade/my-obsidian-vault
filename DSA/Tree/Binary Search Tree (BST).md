## Introduction

A **Binary Search Tree (BST)** is a special type of binary tree where nodes are arranged in a sorted order to allow fast searching, insertion, and deletion operations. Each node has at most two children.

## Properties of a BST

1. **Left Subtree**: Contains only nodes with values **less than** the parent node.
2. **Right Subtree**: Contains only nodes with values **greater than** the parent node.
3. **No Duplicate Values**: BSTs do not allow duplicate values.
4. **Inorder Traversal**: Always gives elements in **sorted order**.
5. **Height-Balanced BST**: Ensures O(log n) search complexity in optimal cases.

## Structure of a BST Node

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

## Operations on BST

### 1. **Insertion Operation**

- If the BST is empty, create a root node.
- Otherwise, compare the new key with the root.
    - If smaller, insert in the left subtree.
    - If larger, insert in the right subtree.

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

- If the key matches the root, return the root.
- If the key is smaller, search in the left subtree.
- If the key is larger, search in the right subtree.

```python
def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)
```

### 3. **Traversal Methods**

1. **Inorder (Left → Root → Right)** (Sorted order)

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
- Node has **two children**: Replace with the **inorder successor** (smallest node in the right subtree).

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

## Advantages of BST

1. **Efficient Searching**: Faster than an unsorted tree (O(log n) in balanced trees).
2. **Inorder Traversal Gives Sorted Data**.
3. **Supports Dynamic Data**: Unlike arrays, BST allows dynamic insertion and deletion.
4. **Used in Many Applications**: Databases, file indexing, and search engines.

## Disadvantages of BST

1. **Unbalanced BST Can Degrade to O(n) Complexity** (if all elements are inserted in sorted order).
2. **Requires Additional Memory for Pointers**.
3. **Balancing Requires Extra Effort**: Self-balancing trees like **AVL trees** and **Red-Black trees** solve this issue.

## Applications of BST

1. **Database Indexing** – Faster retrieval of records.
2. **Symbol Tables in Compilers** – Efficient lookup of variables and functions.
3. **Network Routing Algorithms** – BST helps in IP address lookup.
4. **Search Autocomplete** – Used in dictionary-based searching.

## Conclusion

- **BST provides fast operations** for insertion, searching, and deletion.
- **Balancing is crucial** for maintaining O(log n) efficiency.
- **Widely used** in databases, search engines, and AI.

Understanding BSTs is **essential for coding interviews** and competitive programming!