class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        n = len(heights)
        left, right = 0, n - 1
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])

            maxWater = max(maxWater, width * height)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return maxWater
