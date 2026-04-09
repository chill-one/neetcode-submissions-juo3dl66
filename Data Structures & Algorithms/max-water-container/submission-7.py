class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = 0, n - 1
        container = 0

        while left < right:
            container = max(min(heights[left], heights[right]) * (right - left),container)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return container