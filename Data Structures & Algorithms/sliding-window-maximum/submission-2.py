class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        max_deq = deque()
        left = 0
        res = []

        for right in range(len(nums)):
            while(len(max_deq) != 0 and nums[max_deq[-1]] < nums[right]):
                max_deq.pop()

            max_deq.append(right)

            if(max_deq[0] < left):
                max_deq.popleft()

            if(right + 1 >= k):
                res.append(nums[max_deq[0]])
                left += 1

        return res