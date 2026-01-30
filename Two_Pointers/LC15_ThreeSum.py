# LeetCode 15 - 3Sum
# Pattern: Sorting + Two Pointers
#
# Problem:
#   Given an integer array nums, return all the unique triplets
#   [nums[i], nums[j], nums[k]] such that:
#     - i != j, j != k, k != i
#     - nums[i] + nums[j] + nums[k] == 0
#   The solution set must not contain duplicate triplets.
#
# Approach:
#   1. Sort the array.
#   2. Iterate through the array and fix one element nums[i].
#      Skip duplicates for i.
#   3. Use two pointers:
#        - j starts at i + 1
#        - k starts at the end.
#   4. Compare nums[j] + nums[k] with -nums[i]:
#        - If equal → store the triplet.
#        - Move j and k while skipping duplicates.
#        - If greater → move k left.
#        - If smaller → move j right.
#
# Time Complexity: O(n^2)
# Space Complexity: O(1) extra space (excluding output list)



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        size = len(nums)
        result = []

        for i in range(size):

            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = size - 1

            while j < k:

                curr_sum = nums[i] + nums[j] + nums[k]

                if curr_sum == 0:

                    result.append([nums[i], nums[j], nums[k]])

                    # Skip duplicates for j
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1

                    # Skip duplicates for k
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    j += 1
                    k -= 1

                elif curr_sum > 0:
                    k -= 1
                else:
                    j += 1

        return result
