"""
Problem  Name: Find Minimum in Rotated Sorted Array
NeetCode Link: https://neetcode.io/problems/find-minimum-in-rotated-sorted-array/question
LeetCode Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description

Time  Complexity: O(logn)
Space Complexity: O(1)

Platform Sync: Class/Method/Variable names & signatures may need minor adjustments
               to match platform-specific requirements.
"""

# ───────────
# SOLUTION 1:
# ───────────
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        left_idx = 0
        right_idx = len(nums) - 1

        while left_idx <= right_idx:
            if nums[left_idx] < nums[right_idx]:
                res = min(res, nums[left_idx])
                break

            middle_idx = (left_idx + right_idx) // 2

            res = min(res, nums[middle_idx])

            if nums[middle_idx] >= nums[left_idx]:
                left_idx = middle_idx + 1
            else:
                right_idx = middle_idx - 1

        return res

# ───────────
# SOLUTION 2:
# ───────────
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left_idx = 0
        right_idx = len(nums) - 1

        while left_idx < right_idx:
            middle_idx = (left_idx + right_idx) // 2

            if nums[middle_idx] < nums[right_idx]:
                right_idx = middle_idx
            else:
                left_idx = middle_idx + 1

        return nums[left_idx]