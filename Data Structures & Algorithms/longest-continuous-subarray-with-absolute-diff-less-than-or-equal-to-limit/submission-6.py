class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        maxSub = 0
        minQueue = deque([])
        maxQueue = deque([])

        for right in range(len(nums)):
            value = nums[right]

            #keep track of the recent min and max
            while minQueue and nums[minQueue[-1]] > value:
                minQueue.pop()
            minQueue.append(right)

            while maxQueue and nums[maxQueue[-1]]  < value:
                maxQueue.pop()
            maxQueue.append(right)

            #shrink the window until the limit is what we want
            if nums[maxQueue[0]] - nums[minQueue[0]] > limit:
                #remove outdated value
                if minQueue[0] == left:
                    minQueue.popleft()

                if maxQueue[0] == left:
                    maxQueue.popleft()
                left += 1

            maxSub = max(right - left + 1, maxSub)


        return maxSub
            
            
                




