class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        maxL, maxR = height[left], height[right]
        res = 0

        while left < right:
            
            if maxL < maxR:
                res += maxL - height[left]
                left += 1
                maxL = max(maxL, height[left])
            else:
                res += maxR - height[right]
                right -= 1
                maxR = max(maxR, height[right])


        return res

            