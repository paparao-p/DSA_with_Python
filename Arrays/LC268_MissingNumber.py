"""
Problem: 268. Missing Number
Difficulty: Easy
Pattern: Bit Manipulation / XOR

Description
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Example:
Input:  nums = [3,0,1]
Output: 2

Input:  nums = [0,1]
Output: 2

Approach (XOR Trick)
1. XOR all numbers from 0 to n.
2. XOR all elements in the array.
3. The missing number will remain after cancellation.

Reason:
a ^ a = 0  
a ^ 0 = a  

So all common numbers cancel out, leaving the missing one.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        xor_all = 0
        xor_arr = 0

        # XOR of all numbers from 0 to n
        for i in range(n + 1):
            xor_all ^= i

        # XOR of array elements
        for num in nums:
            xor_arr ^= num

        return xor_all ^ xor_arr