# LeetCode 74 - Search a 2D Matrix
# Difficulty: Medium
# Pattern: Binary Search (Flattened 1D Approach)
#
# Problem:
#   You are given an m x n integer matrix with the following properties:
#     - Each row is sorted in non-decreasing order.
#     - The first integer of each row is greater than the last integer of the previous row.
#   Given an integer target, return True if target is in matrix, otherwise return False.
#
# Approach:
#   Treat the matrix as a single sorted 1D array.
#   Perform binary search on range [0, rows*cols - 1].
#   Convert 1D index to 2D:
#       row = mid // cols
#       col = mid % cols
#
# Time Complexity: O(log(m*n))
# Space Complexity: O(1)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows * cols - 1

        while low <= high:
            mid = (low + high) // 2
            row = mid // cols
            col = mid % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                high = mid - 1
            else:
                low = mid + 1

        return False