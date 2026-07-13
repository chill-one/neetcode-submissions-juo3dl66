class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        from bisect import bisect_left

        idx = bisect_left(arr, x)

        l, r = idx-1, idx
        res = []
        while (l >= 0 or r < len(arr)) and len(res) != k:
            diff1 = abs(arr[l] - x) if l >= 0 else float('inf')
            diff2 = abs(arr[r] - x) if r < len(arr) else float('inf')
            if diff1 <= diff2:
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1

        return sorted(res)