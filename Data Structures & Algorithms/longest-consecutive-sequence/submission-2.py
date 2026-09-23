class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        uni = set(nums)
        lcs = 0
        for i in uni:
            if i - 1 in uni:
                continue
            count = 1
            while i + 1 in uni:
                count += 1
                i += 1
            lcs = max(count, lcs)
        return lcs