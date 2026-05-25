class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = {i: [] for i in range(n)}


        for src_, dst_, price in flights:
            adjList[src_].append((dst_, price))

        
        ford = [float("inf")] * n 

        ford[src] = 0

        for i in range(k+1):
            temp = list(ford)
            for j in range(n):
                for dst_, price in adjList[j]:
                    if ford[j] != float("inf"):
                        temp[dst_] = min(temp[dst_], ford[j] + price)

            ford = temp
        return ford[dst] if ford[dst] != float("inf") else -1
            