## Introduction

An **AVL Tree** is a self-balancing binary search tree (BST) where the difference between the heights of the left and right subtrees of any node (balance factor) is at most 1. Named after its inventors, Adelson-Velsky and Landis, the AVL tree ensures O(log n) time complexity for search, insert, and delete operations.

## Properties of an AVL Tree

1. **Binary Search Tree Property**: The left child contains smaller values, the right child contains larger values.
2. **Balance Factor**: For any node, `balance factor = height(left subtree) - height(right subtree)`. It should be `-1, 0, or 1`.
3. **Self-Balancing**: If the balance factor becomes less than `-1` or greater than `1`, the tree is rebalanced using rotations.

## Rotations in AVL Tree

To maintain balance, AVL trees use four types of rotations:

1. **Right Rotation (LL Rotation)** - Performed when nodes are inserted into the left subtree of the left child.
2. **Left Rotation (RR Rotation)** - Performed when nodes are inserted into the right subtree of the right child.
3. **Left-Right Rotation (LR Rotation)** - Performed when nodes are inserted into the right subtree of the left child.
4. **Right-Left Rotation (RL Rotation)** - Performed when nodes are inserted into the left subtree of the right child.

## AVL Tree Implementation in Python

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        return node.height if node else 0
    
    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        return x
    
    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        return y
    
    def insert(self, root, key):
        if not root:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        balance = self.get_balance(root)
        
        # Left Heavy (LL Rotation)
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)
        
        # Right Heavy (RR Rotation)
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)
        
        # Left-Right Heavy (LR Rotation)
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        
        # Right-Left Heavy (RL Rotation)
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        
        return root
```

## Operations on AVL Tree

### 1. **Insertion** (O(log n))

- Insert like a BST.
- Check balance factor and apply appropriate rotations if needed.

### 2. **Deletion** (O(log n))

- Delete like a BST.
- Recalculate balance and perform necessary rotations.

### 3. **Search** (O(log n))

- Search is similar to a BST since AVL maintains order.

## Applications of AVL Tree

1. **Databases and File Systems** - Used for indexing to maintain fast search times.
2. **Memory Management** - Used in dynamic memory allocation.
3. **Routing Algorithms** - Applied in network routing protocols.
4. **Symbol Tables** - Used in compilers and interpreters.

## Time Complexity

|Operation|Complexity|
|---|---|
|Insert|O(log n)|
|Delete|O(log n)|
|Search|O(log n)|

## Conclusion

- **AVL trees maintain balance to ensure O(log n) operations.**
- **They provide faster search times than unbalanced BSTs.**
- **Used in applications requiring fast and frequent lookups.**