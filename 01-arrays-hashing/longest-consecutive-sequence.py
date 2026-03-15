# Problem  Name: Longest Consecutive Sequence
# NeetCode Link: https://neetcode.io/problems/longest-consecutive-sequence/question
# LeetCode Link: https://leetcode.com/problems/longest-consecutive-sequence/description

# Time  Complexity: O(nlogn) | O(n) | O(n)
# Space Complexity: O(n)

# Platform Sync: Class/Method/Variable names & signatures may need minor adjustments
#                to match platform-specific requirements.
#
#
#
# SOLUTION 1:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue

            if nums[i] == nums[i + 1] - 1:
                current_streak += 1
            else:
                current_streak = 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak
#
#
#
# SOLUTION 2:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longest_streak = 0

        for num in numSet:
            if (num - 1) not in numSet:
                current_streak = 1

                while (num + current_streak) in numSet:
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
#
#
#
# SOLUTION 3:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        streak_map = defaultdict(int)

        longest_streak = 0

        for num in nums:
            if not streak_map[num]:
                left_streak = streak_map[num - 1]
                right_streak = streak_map[num + 1]

                current_streak = left_streak + right_streak + 1

                streak_map[num] = current_streak

                longest_streak = max(longest_streak, current_streak)

                streak_map[num - left_streak] = current_streak
                streak_map[num + right_streak] = current_streak

        return longest_streak
