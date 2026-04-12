"""
Problem  Name: 3Sum
NeetCode Link: https://neetcode.io/problems/three-integer-sum/question
LeetCode Link: https://leetcode.com/problems/3sum/description

Time  Complexity: O(n^2)
Space Complexity: O(n)

Platform Sync: Class/Method/Variable names & signatures may need minor adjustments
               to match platform-specific requirements.
"""

# ───────────
# SOLUTION 1:
# ───────────
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        freq_count = defaultdict(int)

        for num in nums:
            freq_count[num] += 1

        res = []

        for i in range(len(nums)):
            freq_count[nums[i]] -= 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                freq_count[nums[j]] -= 1

                if j > i + 1 and nums[j] == nums[j - 1]:
                    freq_count[nums[j]] += 1
                    continue

                target = -(nums[i] + nums[j])

                if target in freq_count and freq_count[target]:
                    if target >= nums[j]:
                        res.append([nums[i], nums[j], target])

                freq_count[nums[j]] += 1

            freq_count[nums[i]] += 1

        return res

# ───────────
# SOLUTION 2:
# ───────────
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left_idx = i + 1
            right_idx = len(nums) - 1

            while left_idx < right_idx:
                three_sum = nums[i] + nums[left_idx] + nums[right_idx]

                if three_sum == 0:
                    res.append([nums[i], nums[left_idx], nums[right_idx]])

                    while left_idx < right_idx and nums[left_idx] == nums[left_idx + 1]:
                        left_idx += 1
                    while left_idx < right_idx and nums[right_idx] == nums[right_idx - 1]:
                        right_idx -= 1

                    left_idx += 1
                    right_idx -= 1

                elif three_sum < 0:
                    left_idx += 1

                elif three_sum > 0:
                    right_idx -= 1

        return res