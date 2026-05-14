class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #minHeap to store computation for euclidean distance
        minHeap = []


        #go through the points and compute the euclidean distance and push it to the minHeap
        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(minHeap, [distance, x, y])

        res = []
        #grab k items from the minHeap 
        for i in range(k):
            minVal = heapq.heappop(minHeap)
            res.append(minVal[1:])

        return res
