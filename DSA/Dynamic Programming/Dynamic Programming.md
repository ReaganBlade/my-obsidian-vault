**Overview of Dynamic Programming**
### Introduction to Dynamic Programming

Dynamic Programming (DP) is an optimization technique used to solve complex problems by breaking them down into smaller subproblems. It is particularly useful for problems that exhibit **overlapping subproblems** and **optimal substructure**.

### Characteristics of Dynamic Programming

1. **Overlapping Subproblems**: The problem can be divided into smaller subproblems, and these subproblems are solved multiple times.
2. **Optimal Substructure**: The optimal solution to a problem can be constructed from the optimal solutions of its subproblems.
3. **Memoization or Tabulation**: DP can be implemented using either a top-down (memoization) or bottom-up (tabulation) approach.

### Types of Dynamic Programming Approaches

1. **Top-Down Approach (Memoization)**: Solves the problem recursively and stores intermediate results to avoid redundant calculations.
2. **Bottom-Up Approach (Tabulation)**: Solves subproblems iteratively and stores results in a table, building up to the final solution.

### Common Problems Solved Using DP

1. **Fibonacci Sequence**: Computing Fibonacci numbers efficiently using DP.
2. **Knapsack Problem**: Selecting items with given weights and values to maximize profit within a weight constraint.
3. **Longest Common Subsequence (LCS)**: Finding the longest subsequence common to two sequences.
4. **Coin Change Problem**: Determining the number of ways to make a given amount using available denominations.
5. **Matrix Chain Multiplication**: Finding the optimal order of multiplying matrices to minimize cost.
6. **Subset Sum Problem**: Checking if a subset with a given sum exists in an array.
7. **Edit Distance**: Measuring the minimum number of edits required to convert one string into another.

### DP on Graphs and Trees

- **Shortest Path Problems**: Bellman-Ford and Floyd-Warshall algorithms use DP.
- **Tree DP**: Used for problems like subtree sum, lowest common ancestor, and diameter of a tree.

### Steps to Solve a DP Problem

1. **Define the State**: Identify what each subproblem represents.
2. **Formulate the Recurrence Relation**: Express the problem in terms of smaller subproblems.
3. **Choose the Approach**: Decide between top-down (recursion + memoization) or bottom-up (tabulation).
4. **Optimize Space Complexity**: Reduce unnecessary storage if possible.
5. **Implement and Debug**: Write the code and test with various inputs.

### Conclusion

Dynamic Programming is a powerful algorithmic paradigm used for solving a wide range of computational problems. Mastering DP requires practice, a strong understanding of recursion, and the ability to recognize overlapping subproblems and optimal substructure.

- [[Getting Started (Basic Formulation)]]