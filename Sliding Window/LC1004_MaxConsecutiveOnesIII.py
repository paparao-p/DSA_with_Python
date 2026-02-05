# LeetCode 1004 - Max Consecutive Ones III
# Pattern: Sliding Window (At Most K Zeros)
#
# Problem:
#   Given a binary array nums and an integer k,
#   return the maximum number of consecutive 1's in the array
#   if you can flip at most k zeros.
#
# Approach:
#   Use a sliding window with two pointers:
#     - Expand the right pointer to include new elements.
#     - Track how many zeros are inside the window.
#     - If zero count exceeds k, shrink the window from the left
#       until it becomes valid again.
#     - At every step, update the maximum window size.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        max_len = 0
        right = 0
        left = 0
        zeroes = 0

        while right < len(nums):
            
            if nums[right] != 1:
                zeroes += 1

            while zeroes > k:
                if nums[left] != 1:
                    zeroes -= 1
                left += 1
            
            right += 1
            max_len = max(max_len,right-left)
        
        return max_len
