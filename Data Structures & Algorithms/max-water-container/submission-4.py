class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_water = 0

        while left < right:
            water = (right - left) * min(heights[left], heights[right])

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

            max_water = max(max_water, water)

        return max_water