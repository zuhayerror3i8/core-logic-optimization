# Problem  Name: Valid Palindrome
# NeetCode Link: https://neetcode.io/problems/is-palindrome/question
# LeetCode Link: https://leetcode.com/problems/valid-palindrome/description

# Time  Complexity: O(n)
# Space Complexity: O(n) | O(1)

# Platform Sync: Class/Method/Variable names & signatures may need minor adjustments
#                to match platform-specific requirements.
#
#
#
# SOLUTION 1:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()

        return newStr == newStr[::-1]
#
#
#
# SOLUTION 2:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_idx = 0
        right_idx = len(s) - 1

        while (left_idx < right_idx):
            while (left_idx < right_idx) and not s[left_idx].isalnum():
                left_idx += 1
            while (left_idx < right_idx) and not s[right_idx].isalnum():
                right_idx -= 1

            if s[left_idx].lower() != s[right_idx].lower():
                return False

            left_idx += 1
            right_idx -= 1

        return True
