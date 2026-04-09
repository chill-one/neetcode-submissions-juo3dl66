class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums))]

        dic = {}

        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        for key, value in dic.items():
            bucket[value - 1].append(key)

        res = []
        m = k
        for arr in bucket[::-1]:
            if k <= 0:
                break
            if not arr:
                continue
            for num in arr:
                res.append(num)
                k-= 1

        return res

            

