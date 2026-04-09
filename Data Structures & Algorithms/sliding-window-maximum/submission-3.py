class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        nums[deque[-1]] < nums[right] we keep remove until false
        check if deque[0] is in our bound by comparing to left
        start adding to res when are at the bound of k
        """
        from collections import deque

        window = deque()
        res = []

        left = 0
        for right in range(len(nums)):
            if len(window) > 0 and window[0] < left:
                window.popleft()
            while(len(window) > 0 and nums[window[-1]] < nums[right]):
                window.pop()
            window.append(right)
            if right - left + 1 >= k:
                print(window)
                res.append(nums[window[0]])
                left+=1

        return res
