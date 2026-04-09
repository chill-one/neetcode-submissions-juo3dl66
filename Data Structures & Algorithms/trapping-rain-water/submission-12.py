class Solution:
    def trap(self, height: List[int]) -> int:
        res, n = 0, len(height)

        maxL, maxR = height[0], height[n-1]
        left, right = 0, n - 1
        while left < right:
            
            if maxL < maxR:
                left += 1
                maxL = max(height[left], maxL)
                res += maxL - height[left]
            else:
                right -= 1
                maxR = max(height[right], maxR)
                res += maxR - height[right]
            

        return res