class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        def dfs(i, totalSum):
            if i == len(nums):
                if totalSum == target:
                    return 1 
                else:
                    return 0

            return dfs(i+1, totalSum - nums[i]) + dfs(i+1, totalSum + nums[i])


        return dfs(0, 0)


            