# Problem  Name: Valid Parentheses
# NeetCode Link: https://neetcode.io/problems/validate-parentheses/question
# LeetCode Link: https://leetcode.com/problems/valid-parentheses/description

# Time  Complexity: O(n)
# Space Complexity: O(n)

# Platform Sync: Class/Method/Variable names & signatures may need minor adjustments
#                to match platform-specific requirements.
#
#
#
# OPTIMIZED SOLUTION:
class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []

        for ch in range(len(s)):
            if s[ch] in bracket_map:
                if not stack or stack[-1] != bracket_map[s[ch]]:
                    return False
                stack.pop()
            else:
                stack.append(s[ch])

        return not stack
