class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        [2,1,5,6,2,3]
        maxRect = 2
        [(0 , 1) , (2, 5), (3, 6), ]
        """
        stack = []
        largestRect = 0

        for idx, height in enumerate(heights):
            newIdx = idx
            while stack and stack[-1][1] > height:
                oldIdx, oldheight = stack.pop()
                largestRect = max(largestRect, (idx - oldIdx ) * oldheight)
                newIdx = oldIdx

            stack.append((newIdx, height))

        for idx , height in stack:
            largestRect = max(largestRect, (len(heights) - idx ) * height)

        return largestRect