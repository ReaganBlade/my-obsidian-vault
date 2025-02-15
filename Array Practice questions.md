## **1\. The Treasure Hunt – Find the Missing Number**

Captain Jack Sparrow is on a treasure hunt and has a map with n marked locations numbered from 0 to n. However, one of the location numbers has been smudged, and Jack can't find it. Given the list of location numbers he still has, help Jack find the missing location number so he can claim the treasure.

**Problem Statement:**  
Given an array containing n distinct numbers from 0 to n, find the missing number.

**Constraints:**

* 1 ≤ n ≤ 104  
* 0 ≤ array elements ≤ n

**Examples:**

* Input: arr \= \[3, 0, 1\]  
  Output: 2  
* Input: arr \= \[0, 1\]  
  Output: 2

**Test Cases:**

* Input: arr \= \[9, 6, 4, 2, 3, 5, 7, 0, 1\] → Output: 8  
* Input: arr \= \[0\] → Output: 1  
* Input: arr \= \[1, 2, 3, 4, 5\] → Output: 0

## **2\. The Magical Potion – Maximum Subarray Sum**

Harry is brewing a magical potion in Hogwarts. He needs to select a contiguous sequence of ingredients from his inventory to achieve the highest magical power. Each ingredient has a power level (which can be positive, negative, or zero). Help Harry choose a contiguous subarray of ingredients that yields the highest possible power for his potion.

**Problem Statement:**  
Find the contiguous subarray within an array (containing at least one number) that has the largest sum.

**Constraints:**

* 1 ≤ n ≤ 105  
* \-104 ≤ array elements ≤ 104

**Examples:**

* Input: arr \= \[-2,1,-3,4,-1,2,1,-5,4\]  
  Output: 6 (subarray \[4,-1,2,1\])  
* Input: arr \= \[1\]  
  Output: 1

**Test Cases:**

* Input: arr \= \[5,4,-1,7,8\] → Output: 23  
* Input: arr \= \[-1, \-2, \-3, \-4\] → Output: \-1  
* Input: arr \= \[1, 2, 3, 4, 5\] → Output: 15

## **3\. The Time Machine – Rotate Array**

Professor X has built a time machine that can shift timelines. Given a sequence of n events in history, he wants to shift the timeline to the right by k steps so that future generations experience events in a different order. Help him rotate the array representing these events.

**Problem Statement:**  
Given an array, rotate the array to the right by k steps, where k is non-negative.

**Constraints:**

* 1 ≤ n ≤ 105  
* \-105 ≤ array elements ≤ 105  
* 0 ≤ k ≤ n

**Examples:**

* Input: arr \= \[1,2,3,4,5,6,7\], k \= 3  
  Output: \[5,6,7,1,2,3,4\]  
* Input: arr \= \[-1,-100,3,99\], k \= 2  
  Output: \[3,99,-1,-100\]

**Test Cases:**

* Input: arr \= \[1, 2, 3, 4, 5\], k \= 2 → Output: \[4, 5, 1, 2, 3\]  
* Input: arr \= \[10, 20, 30\], k \= 1 → Output: \[30, 10, 20\]  
* Input: arr \= \[1, 2\], k \= 3 → Output: \[2, 1\]

## **4\. Sherlock’s Case – Two Sum Problem**

Sherlock Holmes is solving a mysterious case where he has n clues, each clue has a specific numerical value. He suspects that exactly two clues add up to a critical target value that will solve the case. Help Sherlock find the indices of these two clues.

**Problem Statement:**  
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. Assume that each input would have exactly one solution.

**Constraints:**

* 2 ≤ n ≤ 105  
* \-109 ≤ array elements ≤ 109  
* \-109 ≤ target ≤ 109

**Examples:**

* Input: nums \= \[2,7,11,15\], target \= 9  
  Output: \[0, 1\]  
* Input: nums \= \[3,2,4\], target \= 6  
  Output: \[1, 2\]

**Test Cases:**

* Input: nums \= \[1,2,3,4\], target \= 7 → Output: \[2,3\]  
* Input: nums \= \[-1,-2,-3,-4,-5\], target \= \-8 → Output: \[2,4\]  
* Input: nums \= \[5,5,5\], target \= 10 → Output: \[0,1\]

## **5\. The Enchanted Forest – Find All Duplicates**  
In the enchanted forest, magical creatures come and go. Each creature has an ID between 1 and n. However, some creatures are mischievous and appear twice, while others appear only once. Help the forest ranger find all the creatures that appear twice.  
**Problem Statement:**  
Given an integer array of size n where 1 ≤ array elements ≤ n, some elements appear twice, and others appear once. Find all the elements that appear twice.

**Constraints:**

* 1 ≤ n ≤ 105  
* 1 ≤ array elements ≤ n

**Examples:**

* Input: arr \= \[4,3,2,7,8,2,3,1\]  
  Output: \[2, 3\]  
* Input: arr \= \[1,1,2\]  
  Output: \[1\]

**Test Cases:**

* Input: arr \= \[3,3,1,4,5,6,7,8,5\] → Output: \[3,5\]  
* Input: arr \= \[1,1,1,2,2,2\] → Output: \[1,2\]  
* Input: arr \= \[1,2,3,4\] → Output: \[\]

1. WAP **Check if Two Arrays Are Equal**

	**Input:**  
		arr1 \= \[1, 2, 3\]  
		arr2 \= \[3, 2, 1\]  
	**Output:** True

#### 2. **WAP to Find the Leader Elements. (Leader Element:** An element is a leader if it is greater than all elements to its right.)

**Input:** \[16, 17, 4, 3, 5, 2\]		**Output:** \[17, 5, 2\]

#### 3. **Rotate Array to the Left by k Positions.**

**Input:**  
	arr \= \[1, 2, 3, 4, 5\]  
k \= 2

**Output:** \[3,4,5,1,2\]

#### 4. **Find Majority Element in given array.** Find the element that appears more than n/2 times.

**Input:** \[3, 3, 4, 2, 4, 4, 2, 4, 4\]			**Output:** 4

#### 5. **Find Peak Element,** A peak element is greater than its neighbors. Find one such element.

**Input:** \[1, 3, 20, 4, 1, 0\]				**Output:** 20

#### 6. **Sort an Array consisting of 0s, 1s, and 2s.**

**Input:** \[2, 0, 2, 1, 1, 0\]				**Output:** \[0,0,1,1,2,2\]