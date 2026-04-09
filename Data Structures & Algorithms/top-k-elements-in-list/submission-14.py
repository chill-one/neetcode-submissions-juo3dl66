class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1


        bucket = [[] for _ in range(len(nums) + 1)]


        for num, count in dic.items():
            bucket[count].append(num)


        res = []

        for i in range(len(bucket)-1, -1, -1):
            if len(res) == k:
                break
            for num in bucket[i]:
                res.append(num)

        return res