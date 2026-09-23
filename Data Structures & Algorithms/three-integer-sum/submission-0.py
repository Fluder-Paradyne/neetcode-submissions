from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        n = len(nums)

        for idx, num in enumerate(nums):
            if num > 0:
                break
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            
            l, r = idx + 1, n - 1
            while l < r:
                total_sum = num + nums[l] + nums[r]
                if total_sum > 0:
                    r -= 1
                if total_sum < 0:
                    l += 1
                if total_sum == 0:
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return result