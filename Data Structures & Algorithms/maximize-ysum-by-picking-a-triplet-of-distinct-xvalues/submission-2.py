class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        h = []
        seen = {}

        for val1, val2 in zip(x, y):
            if val1 not in seen:
                seen[val1] = val2
            else:
                seen[val1] = max(seen[val1], val2)

        if len(seen) < 3:
            return -1

        for val in seen.values():
            heapq.heappush(h, -val)

        return -heapq.heappop(h) + -heapq.heappop(h) + -heapq.heappop(h)