# Problem  Name: Valid Anagram
# NeetCode Link: https://neetcode.io/problems/is-anagram/question
# LeetCode Link: https://leetcode.com/problems/valid-anagram/description

# Time  Complexity: O(n+m)
# Space Complexity: O(1)

# Platform Sync: Class/Method/Variable names & signatures may need minor adjustments
#                to match platform-specific requirements.
#
#
#
# SOLUTION 1:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT
#
#
#
# SOLUTION 2:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)
#
#
#
# SOLUTION 3:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for i in count:
            if i != 0:
                return False
        return True
