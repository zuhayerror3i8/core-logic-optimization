# Problem  Name: Two Sum
# NeetCode Link: https://neetcode.io/problems/two-integer-sum/question
# LeetCode Link: https://leetcode.com/problems/two-sum/description

# Time  Complexity: O(nlogn) | O(n) | O(n)
# Space Complexity: O(n)

# Platform Sync: Class/Method/Variable names & signatures may need minor adjustments
#                to match platform-specific requirements.
#
#
#
# SOLUTION 1:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = []

        for i, num in enumerate(nums):
            indexed_nums.append([num, i])

        indexed_nums.sort()

        i = 0
        j = len(indexed_nums) - 1

        while i < j:
            curr = indexed_nums[i][0] + indexed_nums[j][0]

            if curr == target:
                return [min(indexed_nums[i][1], indexed_nums[j][1]),
                        max(indexed_nums[i][1], indexed_nums[j][1])]
            elif curr < target:
                i += 1
            else:
                j -= 1
#
#
#
# SOLUTION 2:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, num in enumerate(nums):
            prevMap[num] = i

        for i, num in enumerate(nums):
            diff = target - num

            if diff in prevMap and prevMap[diff] != i:
                return [i, prevMap[diff]]
#
#
#
# SOLUTION 3:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[num] = i
