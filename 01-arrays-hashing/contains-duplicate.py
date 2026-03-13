# Problem  Name: Contains Duplicate
# NeetCode Link: https://neetcode.io/problems/duplicate-integer/question
# LeetCode Link: https://leetcode.com/problems/contains-duplicate/description

# Time  Complexity: O(n)
# Space Complexity: O(n)

# Platform Sync: Class/Method/Variable names & signatures may need minor adjustments
#                to match platform-specific requirements.
#
#
#
# SOLUTION 1:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
#
#
#
# SOLUTION 2:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
