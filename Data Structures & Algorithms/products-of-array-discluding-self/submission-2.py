class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        
        n = len(nums)
        prefix_product = [0] * n
        suffix_product = [0] * n
        result = [1] * n

        prefix_product[0] = 1
        for i in range(1, n):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
        
        suffix_product[-1] = 1
        for i in range(n-2, -1, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i +1]

        for i in range(n):
            result[i] = prefix_product[i] * suffix_product[i]
        return result

