# Problem  Name: Encode and Decode Strings
# NeetCode Link: https://neetcode.io/problems/string-encode-and-decode/question
# LeetCode Link: https://leetcode.com/problems/encode-and-decode-strings/description

# Time  Complexity: O(m)
# Space Complexity: O(m+n)

# Platform Sync: Class/Method/Variable names & signatures may need minor adjustments
#                to match platform-specific requirements.
#
#
#
# OPTIMIZED SOLUTION:
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            starting_idx = j + 1
            ending_idx = starting_idx + length

            res.append(s[starting_idx:ending_idx])

            i = ending_idx

        return res
