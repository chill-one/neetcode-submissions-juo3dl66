class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        [[0,1],[2,2],[2,4],[4,5]]

        """
        stack = []
        largest = 0


        for idx, h in enumerate(heights):
            prev_idx = idx
            while stack and stack[-1][1] > h:
                prev_idx, val = stack.pop()
                largest = max(largest, (idx - prev_idx) * val)

            stack.append((prev_idx, h))

        
        for idx, height in stack:
            rect = (len(heights) - idx) * height
            largest = max(rect, largest)

        return largest

    

            

            