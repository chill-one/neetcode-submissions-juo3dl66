class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        #Sort based on start time
        intervals.sort(key=lambda x: x[0])
        #Sorte the quereies based on thier 
        sorted_queries = sorted([(val, i) for i, val in enumerate(queries)], key=lambda x:x[0])

        #min-heap
        heap = []
        
        res = [-1 for _ in range(len(queries))]
        left = 0
        for querie, idx in sorted_queries:
            while left < len(intervals) and intervals[left][0] <= querie:
                length = intervals[left][1] - intervals[left][0] + 1
                heapq.heappush(heap, (length, intervals[left][0]))
                left += 1

            
            while heap:
                length, start = heap[0]
                if start <= querie <= start + length - 1:
                    res[idx] = length
                    break
                else:
                    heapq.heappop(heap)

        return res




        



        return res

