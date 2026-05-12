class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = []
        for num in nums:
            self.update(num)
            

    def update(self, num):
        heapq.heappush(self.minHeap, num)
        if self.k < len(self.minHeap):
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        self.update(val)
        return self.minHeap[0]
        
