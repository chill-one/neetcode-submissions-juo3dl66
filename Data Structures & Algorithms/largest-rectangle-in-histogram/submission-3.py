class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        [7, 1, 7, 2, 2, 4]
        [[0, 7], ]
        maxRect = 
        """
        stack = []
        maxRect = 0
        n = len(heights)
        for i, val in enumerate(heights):
            new_idx = i
            while stack and stack[-1][1] > val:
                idx, height = stack.pop()
                currRect = (i - idx ) * height
                maxRect = max(maxRect, currRect)
                new_idx = idx
            stack.append([new_idx, val])

        
        print(stack)
        for idx, height in stack:
            maxRect = max(maxRect, (n - idx) * height)
        return maxRect
            

            


            

                
                


            