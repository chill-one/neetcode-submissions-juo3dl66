class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # You prioritze larger frequency so that smaller frequency can complete its cycle in between 
        count = Counter(tasks)

        time = 0

        maxHeap = []
        queue = deque()

        #push the frequency and they key into the maxHeap to determin the largest frequency
        for key, value in count.items():
            heapq.heappush(maxHeap, -value)


        while maxHeap or queue:
            if queue and time == queue[0][1]:
                value, startTime = queue.popleft()
                heapq.heappush(maxHeap, value)
            
            #processed task
            time += 1
            if maxHeap:
                new_freq = heapq.heappop(maxHeap) + 1
                if new_freq < 0:
                    queue.append((new_freq, time + n))

        return time

            


        


        

        


        



        

        