"""
Problem  Name: Longest Repeating Character Replacement
NeetCode Link: https://neetcode.io/problems/longest-repeating-substring-with-replacement/question
LeetCode Link: https://leetcode.com/problems/longest-repeating-character-replacement/description

Time  Complexity: O(m*n) | O(n)
Space Complexity: O(m)

Platform Sync: Class/Method/Variable names & signatures may need minor adjustments
               to match platform-specific requirements.
"""

# ───────────
# SOLUTION 1:
# ───────────
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)

        res_maxlen = 0

        for ch in charSet:
            count = 0

            left_idx = 0

            for right_idx in range(len(s)):
                if s[right_idx] == ch:
                    count += 1

                while (right_idx - left_idx + 1) - count > k:
                    if s[left_idx] == ch:
                        count -= 1

                    left_idx += 1

                res_maxlen = max(res_maxlen, right_idx - left_idx + 1)

        return res_maxlen

# ───────────
# SOLUTION 2:
# ───────────
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_count = defaultdict(int)

        max_freq = 0

        left_idx = 0

        res_maxlen = 0

        for right_idx in range(len(s)):
            freq_count[s[right_idx]] += 1

            max_freq = max(max_freq, freq_count[s[right_idx]])

            while (right_idx - left_idx + 1) - max_freq > k:
                freq_count[s[left_idx]] -= 1
                left_idx += 1

            res_maxlen = max(res_maxlen, right_idx - left_idx + 1)

        return res_maxlen