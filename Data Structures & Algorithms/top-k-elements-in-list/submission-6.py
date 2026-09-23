from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        h = []
        for key, value in counter.items():
            heapq.heappush(h, ((-1 * value), key))
        
        result = []
        for _ in range(k):
            result.append(heapq.heappop(h)[1])
        return result