class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        res = []

        for right, num in enumerate(nums):
            heapq.heappush(maxHeap, (-num, right))
            if right >= k - 1:
                while maxHeap[0][-1] <= right - k:
                    heapq.heappop(maxHeap)

                res.append(-maxHeap[0][0])

        return res


            
            