class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = {i: [] for i in range(n)}


        for src_, dst_, price in flights:
            adjList[src_].append((dst_, price))


        h = [(0, 0, src)]
        cheapest  = float("inf")

        while h:
            current_price , current_k, current_src = heapq.heappop(h)

            if current_src == dst:
                cheapest = min(cheapest, current_price)
                continue

            if current_k > k or current_price > cheapest:
                continue

            for n_dst, n_price in adjList[current_src]:
                heapq.heappush(h, (current_price + n_price, current_k + 1, n_dst))

        return cheapest if cheapest != float("inf") else -1
            