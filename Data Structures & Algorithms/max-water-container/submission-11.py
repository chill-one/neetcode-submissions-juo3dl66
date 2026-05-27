class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        maxWater = 0
        while left < right:
            if heights[left] < heights[right]:
                water = heights[left] * (right - left)
                maxWater = max(maxWater, water)
                left += 1
            else:
                water = heights[right] * (right - left)
                maxWater = max(maxWater, water)
                right -= 1
        
        return maxWater