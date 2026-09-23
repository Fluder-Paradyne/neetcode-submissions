from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        buckets = [[] for i in range(len(nums) + 1)]
        for num in nums:
            counter[num] += 1
        for num, count in counter.items():
            buckets[count].append(num)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for bucket in buckets[i]:
                res.append(bucket)
                if len(res) == k:
                    return res
