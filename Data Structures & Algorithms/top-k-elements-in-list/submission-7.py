from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        heap = []
        for key, value in counter.items():
            heapq.heappush(heap, ((-1 * value), key))
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result