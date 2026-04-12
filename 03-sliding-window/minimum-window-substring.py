"""
Problem  Name: Minimum Window Substring
NeetCode Link: https://neetcode.io/problems/minimum-window-with-characters/question
LeetCode Link: https://leetcode.com/problems/minimum-window-substring/description

Time  Complexity: O(n+m)
Space Complexity: O(m)

Platform Sync: Class/Method/Variable names & signatures may need minor adjustments
               to match platform-specific requirements.
"""

# ───────────────────
# OPTIMIZED SOLUTION:
# ───────────────────
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_freq = defaultdict(int)

        for ch in t:
            target_freq[ch] += 1

        required = len(target_freq)

        left_idx = 0
        right_idx = 0

        formed = 0

        window_freq = defaultdict(int)

        min_left = 0
        min_len = float("infinity")

        while right_idx < len(s):
            ch = s[right_idx]
            window_freq[ch] += 1

            if ch in target_freq and target_freq[ch] == window_freq[ch]:
                formed += 1

            while left_idx <= right_idx and formed == required:
                if (right_idx - left_idx + 1) < min_len:
                    min_len = right_idx - left_idx + 1
                    min_left = left_idx

                left_char = s[left_idx]
                window_freq[left_char] -= 1

                if left_char in target_freq and target_freq[left_char] > window_freq[left_char]:
                    formed -= 1

                left_idx += 1

            right_idx += 1

        if min_len == float("infinity"):
            return ""
        else:
            return s[min_left:min_left + min_len]