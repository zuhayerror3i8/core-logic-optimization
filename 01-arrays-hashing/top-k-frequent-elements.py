# Problem  Name: Top K Frequent Elements
# NeetCode Link: https://neetcode.io/problems/top-k-elements-in-list/question
# LeetCode Link: https://leetcode.com/problems/top-k-frequent-elements/description

# Time  Complexity: O(nlogn) | O(nlogk) | O(n)
# Space Complexity: O(n) | O(n+k) | O(n)

# Platform Sync: Class/Method/Variable names & signatures may need minor adjustments
#                to match platform-specific requirements.
#
#
#
# SOLUTION 1:
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        freq_pairs = []

        for num, cnt in count.items():
            freq_pairs.append([cnt, num])

        freq_pairs.sort()

        res = []

        while len(res) < k:
            res.append(freq_pairs.pop()[1])
        return res
#
#
#
# SOLUTION 2:
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        min_heap = []

        for num, cnt in count.items():
            heapq.heappush(min_heap, (cnt, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        res = []

        while min_heap:
            res.append(heapq.heappop(min_heap)[1])
        return res
#
#
#
# SOLUTION 3:
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        buckets = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, cnt in count.items():
            buckets[cnt].append(num)

        res = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
