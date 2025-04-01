## Introduction

A **B-Tree** is a **self-balancing search tree** commonly used in databases and file systems to store and manage large blocks of data. It extends the concept of a binary search tree by allowing nodes to have more than two children.

## Properties of B-Tree

A B-Tree of order `m` has the following properties:

1. Each node can have at most `m` children.
2. Each node (except root) must have at least `ceil(m/2)` children.
3. The root must have at least **2 children** if it is not a leaf node.
4. A node with `k` children contains `k-1` keys.
5. Keys within a node are sorted in **ascending order**.
6. All leaves are at the same level (i.e., it is a balanced tree).

## Structure of a B-Tree Node

Each node consists of:

- A list of **keys** (`K1, K2, ..., Kt` where `t` is the number of keys in the node)
- A list of **child pointers** (`C0, C1, ..., Ct` where `Cj` points to the subtree between `Kj` and `Kj+1`)
- A **boolean flag** indicating if it is a leaf node

## Operations on B-Tree

### 1. **Search Operation**

The search operation is similar to binary search but works within a multi-way tree.

```python
class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self, t):  # t is the minimum degree
        self.root = BTreeNode(True)
        self.t = t

    def search(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return node
        if node.leaf:
            return None
        return self.search(node.children[i], key)
```

### 2. **Insertion Operation**

1. Insert the key into the correct position in a **leaf node**.
2. If the node overflows, split it into two nodes and move the middle key up.

```python
    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t - 1):  # If root is full
            new_node = BTreeNode(False)
            new_node.children.append(self.root)
            self.split_child(new_node, 0)
            self.root = new_node
        self.insert_non_full(self.root, key)
    
    def insert_non_full(self, node, key):
        if node.leaf:
            node.keys.append(key)
            node.keys.sort()
        else:
            i = len(node.keys) - 1
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t - 1):
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key)
    
    def split_child(self, parent, index):
        t = self.t
        child = parent.children[index]
        new_node = BTreeNode(child.leaf)
        parent.keys.insert(index, child.keys[t-1])
        parent.children.insert(index + 1, new_node)
        new_node.keys = child.keys[t:]
        child.keys = child.keys[:t-1]
        if not child.leaf:
            new_node.children = child.children[t:]
            child.children = child.children[:t]
```

### 3. **Deletion Operation**

Deletion in a B-Tree is more complex and consists of multiple cases:

1. If the key is in a **leaf node**, remove it directly.
2. If the key is in an **internal node**:
    - Replace it with its **predecessor** (largest in left subtree) or **successor** (smallest in right subtree).
    - If replacement is not possible, **merge nodes** and recurse.

```python
    def delete(self, key):
        self.delete_node(self.root, key)
        if len(self.root.keys) == 0 and not self.root.leaf:
            self.root = self.root.children[0]
    
    def delete_node(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            if node.leaf:
                node.keys.pop(i)
            else:
                node.keys[i] = self.get_predecessor(node.children[i])
                self.delete_node(node.children[i], node.keys[i])
        elif not node.leaf:
            self.delete_node(node.children[i], key)
    
    def get_predecessor(self, node):
        while not node.leaf:
            node = node.children[-1]
        return node.keys[-1]
```

## Time Complexity

|Operation|Average Case|Worst Case|
|---|---|---|
|Search|O(log n)|O(log n)|
|Insert|O(log n)|O(log n)|
|Delete|O(log n)|O(log n)|

## Applications of B-Trees

1. **Databases** – Used for indexing large datasets.
2. **File Systems** – Helps in managing disk storage efficiently.
3. **Search Engines** – Stores and retrieves large amounts of data efficiently.

## Conclusion

- B-Trees optimize search, insert, and delete operations by ensuring balance.
- They are widely used in disk-based storage systems due to their efficiency in handling large datasets.
- Understanding B-Trees is crucial for **interviews** related to **databases, file systems, and large-scale applications**.