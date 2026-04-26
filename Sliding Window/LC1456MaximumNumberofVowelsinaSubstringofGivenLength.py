"""
Problem: 1456. Maximum Number of Vowels in a Substring of Given Length
Difficulty: Medium
Pattern: Sliding Window (Fixed Size)

Description
Given a string s and an integer k, return the maximum number of vowel letters
in any substring of s with length k.

Vowels in English are: 'a', 'e', 'i', 'o', 'u'.

Example:
Input:  s = "abciiidef", k = 3
Output: 3

Explanation:
Substring "iii" contains 3 vowels.

Approach
1. Use a sliding window of size k.
2. Count vowels in the current window.
3. Expand window by adding right character.
4. Shrink window if size exceeds k.
5. Track the maximum vowel count.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = {"a", "e", "i", "o", "u"}
        left = 0
        count = 0
        result = 0

        for right in range(len(s)):

            # Add right character
            if s[right] in vowels:
                count += 1

            # Maintain window size
            if right - left + 1 > k:
                if s[left] in vowels:
                    count -= 1
                left += 1

            # Update result
            result = max(result, count)

        return result