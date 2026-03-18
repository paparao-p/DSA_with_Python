"""
Problem: 739. Daily Temperatures
Difficulty: Medium
Pattern: Monotonic Stack

Description
Given an array of integers temperatures representing daily temperatures,
return an array answer such that answer[i] is the number of days you have
to wait after the ith day to get a warmer temperature.

If there is no future day for which this is possible, keep answer[i] = 0.

Example:
Input:  [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Approach
Use a monotonic decreasing stack (stores indices).

1. Traverse the array.
2. While current temperature is greater than the temperature at the index
   on top of the stack:
      - Pop the index.
      - Calculate days waited (current_index - popped_index).
3. Push current index into the stack.
4. Remaining indices have no warmer day → already 0.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []  # stores indices
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                result[index] = i - index

            stack.append(i)

        return result