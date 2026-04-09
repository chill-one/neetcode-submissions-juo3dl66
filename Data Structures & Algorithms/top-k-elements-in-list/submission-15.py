class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dic = {}

        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        bucket = [[] for _ in range(n + 1)]

        for num, count in dic.items():
            bucket[count].append(num)

        res = []
        for i in range(n, -1, -1):
            list_ = bucket[i]
            while len(res) < k and list_:
                res.append(list_.pop())

            if len(res) == k:
                return res

        return []
            

            


        


