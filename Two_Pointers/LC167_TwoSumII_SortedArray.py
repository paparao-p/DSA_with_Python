# LeetCode 167 - Two Sum II: Input Array Is Sorted
# Pattern: Two Pointers
#
# Problem:
#   Given a 1-indexed sorted array of integers `numbers` and an integer `target`,
#   return the indices (1-based) of the two numbers such that they add up to target.
#   It is guaranteed that exactly one solution exists.
#
# Approach:
#   Use two pointers:
#     - Left pointer `i` starts at the beginning.
#     - Right pointer `j` starts at the end.
#   If numbers[i] + numbers[j] == target → return indices.
#   If the sum is greater than target → move right pointer left.
#   If the sum is smaller than target → move left pointer right.
#
# Time Complexity: O(n)
# Space Complexity: O(1)



class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i = 0
        j = len(numbers) - 1

        while i < j:
            curr_sum = numbers[i] + numbers[j]

            if curr_sum == target:
                return [i + 1, j + 1]
            elif curr_sum > target:
                j -= 1
            else:
                i += 1
