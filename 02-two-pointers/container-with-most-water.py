# Problem  Name: Container With Most Water
# NeetCode Link: https://neetcode.io/problems/max-water-container/question
# LeetCode Link: https://leetcode.com/problems/container-with-most-water/description

# Time  Complexity: O(n)
# Space Complexity: O(1)

# Platform Sync: Class/Method/Variable names & signatures may need minor adjustments
#                to match platform-specific requirements.
#
#
#
# OPTIMIZED SOLUTION:
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_idx = 0
        right_idx = len(heights) - 1

        res = 0

        while left_idx < right_idx:
            current_area = min(heights[left_idx], heights[right_idx]) * (right_idx - left_idx)

            res = max(res, current_area)

            if (heights[left_idx] <= heights[right_idx]):
                left_idx += 1
            else:
                right_idx -= 1

        return res
