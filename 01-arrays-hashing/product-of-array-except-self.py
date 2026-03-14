# Problem  Name: Product of Array Except Self
# NeetCode Link: https://neetcode.io/problems/products-of-array-discluding-self/question
# LeetCode Link: https://leetcode.com/problems/product-of-array-except-self/description

# Time  Complexity: O(n)
# Space Complexity: O(n)

# Platform Sync: Class/Method/Variable names & signatures may need minor adjustments
#                to match platform-specific requirements.
#
#
#
# OPTIMIZED SOLUTION:
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
