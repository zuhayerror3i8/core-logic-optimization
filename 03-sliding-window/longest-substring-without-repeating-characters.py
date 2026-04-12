"""
Problem  Name: Longest Substring Without Repeating Characters
NeetCode Link: https://neetcode.io/problems/longest-substring-without-duplicates/question
LeetCode Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description

Time  Complexity: O(n)
Space Complexity: O(m)

Platform Sync: Class/Method/Variable names & signatures may need minor adjustments
               to match platform-specific requirements.
"""

# ───────────
# SOLUTION 1:
# ───────────
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()

        left_idx = 0

        res_maxlen = 0

        for right_idx in range(len(s)):
            while s[right_idx] in charSet:
                charSet.remove(s[left_idx])
                left_idx += 1

            charSet.add(s[right_idx])

            res_maxlen = max(res_maxlen, len(charSet))

        return res_maxlen

# ───────────
# SOLUTION 2:
# ───────────
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen = {}

        left_idx = 0

        res_maxlen = 0

        for right_idx in range(len(s)):
            if s[right_idx] in lastSeen:
                left_idx = max(left_idx, lastSeen[s[right_idx]] + 1)

            lastSeen[s[right_idx]] = right_idx

            res_maxlen = max(res_maxlen, right_idx - left_idx + 1)

        return res_maxlen