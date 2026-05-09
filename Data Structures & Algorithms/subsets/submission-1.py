class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(pos, curr):
            if pos == len(nums):
                res.append(curr)
                return
            
            #include the first element 
            curr.append(nums[pos])
            dfs(pos + 1, curr[:])
            curr.pop()
            #dont include the current element
            dfs(pos+1, curr[:])

        dfs(0,[])
        return res

            

            