class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = []
        n = len(nums)

        for i in range(n):
            bucket.append([])

        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        for key, value in dic.items():
            bucket[value - 1].append(key)

        res = []
        for buc in bucket[::-1]:
            if len(res) == k:
                break
            for num in buc:
                res.append(num)


        return res

    

