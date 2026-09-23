class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total_water = 0
        l, r = 0, n - 1
        left_wall = height[l]
        right_wall = height[r]
        while l < r:
            if left_wall < right_wall:
                l += 1
                left_wall = max(left_wall, height[l])
                total_water += left_wall - height[l]
            else:
                r -= 1
                right_wall = max(right_wall, height[r])
                total_water += right_wall - height[r]
        return total_water