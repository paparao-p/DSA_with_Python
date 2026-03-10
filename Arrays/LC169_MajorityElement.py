"""
Problem: 169. Majority Element
Difficulty: Easy
Pattern: Boyer-Moore Voting Algorithm

Description
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example:
Input:  nums = [3,2,3]
Output: 3

Input:  nums = [2,2,1,1,1,2,2]
Output: 2

Approach
Use the Boyer-Moore Voting Algorithm.

Idea:
1. Maintain a candidate element and a count.
2. If count becomes 0, select the current element as the new candidate.
3. If the current number equals the candidate → increase count.
4. Otherwise → decrease count.

Because the majority element appears more than n/2 times,
it will always remain as the final candidate.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        candidate = None
        count = 0

        for num in nums:

            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate