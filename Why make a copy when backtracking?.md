Leetcode 77

```
# 77. Combinations

from typing import List

class Solution:

def findCombinations(self, start, end, size, cur, res):

print(cur)

if len(cur) == size:

res.append(cur[:])

return

  

if len(cur) > size:

return

for i in range(start, end + 1):

cur.append(i)

self.findCombinations(i + 1, end, size, cur, res)

cur.pop()

  

def combine(self, n: int, k: int) -> List[List[int]]:

result = []

  

self.findCombinations(1, n, k, [], result)

  

return result
```