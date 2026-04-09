class Solution:
    def trap(self, height: List[int]) -> int:
        """
            The idea is to have a left and right pointer while keeping track of both left max and 
            right max. Each time you shift based on if left or right is greater while comparting
            the value at left and right pointer with thier respective max. Also incremete the result 
            everytime based of left or right max minus the value at thier respective pointers
        """
        
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        res = 0

        while(l < r):
            if maxL <= maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL -  height[l]
            elif maxL > maxR:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR -  height[r]


        return res


