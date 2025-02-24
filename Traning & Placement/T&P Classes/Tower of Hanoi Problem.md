
<img title="a title" alt="Alt text" src="./assets/tower-of-hanoi-python.gif">
The **Tower of Hanoi** problem can be efficiently solved using stacks, which naturally align with the recursive and iterative approaches needed for the problem. Below, I will explain both approaches in detail.

---

## **Problem Statement**

The **Tower of Hanoi** consists of three rods (A, B, and C) and **N** disks of different sizes placed on one rod (source) in decreasing order (largest at the bottom). The goal is to move all disks from the source rod to the destination rod using an auxiliary rod, following these rules:

1. Only one disk can be moved at a time.
2. A larger disk cannot be placed on a smaller disk.
3. You can use the auxiliary rod to temporarily hold disks.

---

## **Approach 1: Recursive Solution using Stack (Function Call Stack)**

In the standard **recursive approach**, the system call stack is inherently used to manage recursive calls. The solution follows this pattern:

1. Move the top `N-1` disks from **source** to **auxiliary** using **destination** as a helper.
2. Move the `Nth` (largest) disk from **source** to **destination**.
3. Move the `N-1` disks from **auxiliary** to **destination** using **source** as a helper.

### **Recursive Code (Implicit Stack)**

```python
def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    
    # Move top n-1 disks from source to auxiliary
    tower_of_hanoi(n-1, source, destination, auxiliary)
    
    # Move the nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")
    
    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n-1, auxiliary, source, destination)

# Example Usage
n = 3
tower_of_hanoi(n, 'A', 'B', 'C')
```

### **Time Complexity**

- The recurrence relation is: T(n)=2T(n−1)+1T(n) = 2T(n-1) + 1
- This simplifies to O(2n)O(2^n), which is exponential.

### **Space Complexity**

- The function call stack grows up to O(n)O(n) due to recursion.

---

## **Approach 2: Iterative Solution using Explicit Stack**

Instead of relying on recursion, we can **simulate the recursion using a stack**. This approach is particularly useful when we want to avoid stack overflow in deep recursion scenarios.

### **Key Idea**

- Each move in the recursive approach corresponds to an entry in a stack.
- We use a stack data structure to keep track of moves instead of using the call stack.

### **Algorithm**

1. **Initialize the Stack**: Use a custom stack to store the state of each function call manually.
2. **Simulate Recursive Calls**: Push the recursive states into the stack and process them iteratively.
3. **Perform Moves**: Extract the moves from the stack and print them.

---

### **Iterative Code using Stack**

```python
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop() if self.stack else None
    
    def is_empty(self):
        return len(self.stack) == 0

def tower_of_hanoi_iterative(n, source, auxiliary, destination):
    stack = Stack()
    
    # Push initial state
    stack.push((n, source, auxiliary, destination))
    
    while not stack.is_empty():
        n, src, aux, dest = stack.pop()

        if n == 1:
            print(f"Move disk 1 from {src} to {dest}")
        else:
            # Push calls in reverse order (to simulate recursion correctly)
            stack.push((n-1, aux, src, dest))  # Move n-1 from aux to dest
            stack.push((1, src, aux, dest))    # Move nth disk
            stack.push((n-1, src, dest, aux))  # Move n-1 from src to aux

# Example Usage
n = 3
tower_of_hanoi_iterative(n, 'A', 'B', 'C')
```

### **Time Complexity**

- Same as the recursive version: O(2n)O(2^n)

### **Space Complexity**

- Since we use an explicit stack, worst-case space usage is O(n)O(n).

---

## **Approach 3: Iterative Solution using Three Stacks**

Instead of using a single stack to simulate recursion, we can solve **Tower of Hanoi** iteratively using three actual **stacks**, one for each rod.

### **Algorithm**

1. **Initialize Three Stacks**:
    
    - **Source Stack**: Contains disks from largest to smallest.
    - **Auxiliary Stack**: Initially empty.
    - **Destination Stack**: Initially empty.
2. **Number of Moves**: The minimum number of moves required is 2n−12^n - 1.
    
3. **Rules to Follow**:
    
    - Move **smallest disk first**.
    - Follow a cyclic order of moves:
        1. Move between **source** and **destination**.
        2. Move between **source** and **auxiliary**.
        3. Move between **auxiliary** and **destination**.
4. **Constraints**:
    
    - Only **valid moves** are allowed (smaller disk on top of a larger disk).

---

### **Iterative Code Using Three Stacks**

```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else float('inf')  # Large value represents empty stack

    def peek(self):
        return self.stack[-1] if self.stack else float('inf')

    def is_empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return str(self.stack)

def move_disk(src, dest, s_name, d_name):
    top1 = src.pop()
    top2 = dest.pop()

    if top1 == float('inf'):
        src.push(top2)
        print(f"Move disk {top2} from {d_name} to {s_name}")
    elif top2 == float('inf'):
        dest.push(top1)
        print(f"Move disk {top1} from {s_name} to {d_name}")
    elif top1 > top2:
        src.push(top1)
        src.push(top2)
        print(f"Move disk {top2} from {d_name} to {s_name}")
    else:
        dest.push(top2)
        dest.push(top1)
        print(f"Move disk {top1} from {s_name} to {d_name}")

def tower_of_hanoi_three_stacks(n):
    source = Stack()
    auxiliary = Stack()
    destination = Stack()

    # Push disks to source stack
    for i in range(n, 0, -1):
        source.push(i)

    s, a, d = "A", "B", "C"

    moves = (2**n) - 1

    if n % 2 == 0:
        d, a = a, d  # Swap destination and auxiliary for even disks

    for i in range(1, moves + 1):
        if i % 3 == 1:
            move_disk(source, destination, s, d)
        elif i % 3 == 2:
            move_disk(source, auxiliary, s, a)
        else:
            move_disk(auxiliary, destination, a, d)

# Example Usage
n = 3
tower_of_hanoi_three_stacks(n)
```

---

## **Conclusion**

- **Recursive Approach** uses the system call stack implicitly.
- **Iterative Approach with Stack** simulates recursion explicitly.
- **Iterative Approach with Three Stacks** follows cyclic moves for efficiency.

Each approach has the same **time complexity** of O(2n)O(2^n) but differs in space efficiency.