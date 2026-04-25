"""
Problem: 1710. Maximum Units on a Truck
Difficulty: Easy
Pattern: Greedy + Sorting

Description
You are given boxTypes, where each boxTypes[i] = [numberOfBoxes, unitsPerBox],
and an integer truckSize.

Return the maximum total number of units that can be put on the truck.

You can choose any boxes, but the total number of boxes must not exceed truckSize.

Example:
Input:  boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8

Explanation:
Take:
1 box of type [1,3] → 3 units  
2 boxes of type [2,2] → 4 units  
1 box of type [3,1] → 1 unit  
Total = 8

Approach
1. Sort boxTypes by units per box in descending order.
2. Pick boxes greedily from highest unit value.
3. Take as many as possible without exceeding truck size.
4. Accumulate total units.

Time Complexity: O(n log n)
Space Complexity: O(1)
"""


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        # Sort by units per box in descending order
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        total_units = 0

        for boxes, units in boxTypes:

            if truckSize == 0:
                break

            # Take maximum possible boxes
            take = min(boxes, truckSize)

            total_units += take * units
            truckSize -= take

        return total_units