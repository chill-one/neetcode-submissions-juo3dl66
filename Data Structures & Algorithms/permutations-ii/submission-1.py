class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        freq = Counter(nums)
        res = []
        def dfs(path):

            if len(path) == len(nums):
                res.append(path[:])
                return 

            for key in freq.keys():
                if freq[key] > 0:
                    path.append(key)
                    freq[key] -= 1

                    dfs(path)

                    freq[key] += 1
                    path.pop()
            

        dfs([])

        return res