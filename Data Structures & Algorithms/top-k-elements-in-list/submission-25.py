class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for _ in range(len(nums) + 1)]

        freq = Counter(nums)
        for key, value in freq.items():
            arr[value].append(key)


        curr = k
        res = []
        print(arr)
        for num in arr[::-1]:
            if curr == 0:
                break
            while num and curr > 0:
                res.append(num.pop())
                curr -=1

        return res
