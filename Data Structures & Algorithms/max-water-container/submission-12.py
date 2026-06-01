class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        water = 0

        while left < right:
            if heights[left] < heights[right]:
                currWater = heights[left] * (right - left)
                water = max(water, currWater)
                left += 1
            else:
                currWater = heights[right] * (right - left)
                water = max(water, currWater)
                right -= 1


        return water