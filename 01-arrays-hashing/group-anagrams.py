# Problem  Name: Group Anagrams
# NeetCode Link: https://neetcode.io/problems/anagram-groups/question
# LeetCode Link: https://leetcode.com/problems/group-anagrams/description

# Time  Complexity: O(m*nlogn) | O(m*n)
# Space Complexity: O(m*n)

# Platform Sync: Class/Method/Variable names & signatures may need minor adjustments
#                to match platform-specific requirements.
#
#
#
# SOLUTION 1:
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for str in strs:
            sortedS = ''.join(sorted(str))
            res[sortedS].append(str)
        return list(res.values())
#
#
#
# SOLUTION 2:
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for str in strs:
            count = [0] * 26

            for ch in str:
                count[ord(ch) - ord('a')] += 1
            res[tuple(count)].append(str)
        return list(res.values())
