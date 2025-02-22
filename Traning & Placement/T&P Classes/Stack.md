Date: Monday Feb 17, 2025

## What is a Stack?

A stack is an abstract data type (ADT) with two primary operations:

- **Push**: Adds an element to the top of the stack.
- **Pop**: Removes the top element from the stack.
	
By Default Stack are dynamic in Python, You can create static Stack.
### Key Properties:

- Follows LIFO (Last In, First Out) principle.
- Can be implemented using arrays or linked lists.
- Used in recursion, expression evaluation, backtracking, etc.

## Applications of Stack

- **Function call management (Recursion)**. -> Tower of Hanoi Problem
- **Undo/Redo operations in editors**.
- **Expression evaluation (Infix to Postfix, Prefix conversion)**.
- **Backtracking (Maze solving, N-Queens Problem)**. -> 
- **Web browser history (Back and Forward navigation)**.
- **Memory Management** 
- **Polish Notations**
- **Symbol** - Paranthesis Balance 


## **Polish Notation**

Polish notation is a way of writing mathematical expressions without the need for parentheses to indicate order of operations.

### **Types of Polish Notation:**

1. **Prefix Notation (Polish Notation)**
    
    - The operator is placed before the operands.
    - Example: `+ 3 4` (which is equivalent to `3 + 4` in infix notation).
2. **Postfix Notation (Reverse Polish Notation - RPN)**
    
    - The operator is placed after the operands.
    - Example: `3 4 +` (which is equivalent to `3 + 4` in infix notation).
3. **Infix Notation (Standard Notation)**
    
    - The operator is placed between the operands.
    - Example: `3 + 4`.

### **Uses of Polish Notation:**

- **Expression Evaluation**: Used in compilers and calculators for fast mathematical computations.
- **Stack-Based Computing**: Used in stack-based programming languages and interpreters (e.g., PostScript).
- **Abstract Syntax Trees (ASTs)**: Helps in parsing expressions in programming languages.
- **Reverse Polish Notation (RPN) Calculators**: Used in HP calculators for efficient evaluation without needing parentheses.
- **Programming Language Design**: Some languages and scripting tools use it for expression evaluation (e.g., Lisp).

Polish notation eliminates the need for parentheses and follows strict order execution, making it efficient for parsing and evaluating expressions.

**Reverse Polish Notation (RPN)** (Postfix notation) is the most commonly used Polish notation today.

### **Why RPN is Popular?**

- **Used in Stack-Based Computation:** Many programming languages, interpreters, and calculators use RPN because it allows easy evaluation using stacks.
- **Efficient for Parsing & Compilers:** Eliminates the need for parentheses, reducing parsing complexity in compilers and expression evaluators.
- **RPN Calculators:** Hewlett-Packard (HP) and other scientific calculators still use RPN for efficient calculations.
- **PostScript & Forth Programming Languages:** These languages use RPN for execution efficiency.

**Prefix Notation** (Polish notation) is mostly used in Abstract Syntax Trees (ASTs) and Lisp-like languages but is less common in practical applications compared to RPN.


 
