# LC238 - Product of Array Except Self
# LeetCode 238 | Medium
# Pattern: Prefix Product + Suffix Product (Space Optimized)


"""
Product of Array Except Self

Given an integer array nums, return an array answer such that:
    answer[i] is equal to the product of all elements of nums
    except nums[i].

Constraints:
- Do not use division.
- Must run in O(n) time.

Approach:
1. First pass (Prefix):
   answer[i] stores product of elements before index i.

2. Second pass (Suffix):
   Maintain a running suffix product.
   Multiply it with existing prefix value.

This avoids using extra prefix and suffix arrays.

Time Complexity: O(n)
Space Complexity: O(1) (excluding output array)
"""



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        answer = [1] * n
        
        # Prefix
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]
        
        # Suffix
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer