class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        #Add all the stone to the heap
        for stone in stones:
            heapq.heappush(maxHeap, -stone)

        #take two heavist stones 
        while len(maxHeap) > 1:
            first = -heapq.heappop(maxHeap)
            second = -heapq.heappop(maxHeap)


            if first > second:
                heapq.heappush(maxHeap, -(first - second))

        
        return -maxHeap[0] if maxHeap else 0
