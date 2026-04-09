class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)

        for num in nums:
            dic[num] += 1

        freq = [[] for _  in range(len(nums))] 
        for key, value in dic.items():
            freq[value-1].append(key)
        print(freq)
        res = []
        for i in range(len(freq)-1, -1, -1):
            if freq[i] and k > 0:
                for j in range(len(freq[i])):
                    if k <= 0:
                        break
                    res.append(freq[i][j])
                    k -= 1


        return res


        
        