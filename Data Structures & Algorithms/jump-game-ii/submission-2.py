class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        def dfs(jump, curr):
            if curr >= len(nums) - 1:
                return jump

            res = len(nums)
            for i in range(1, nums[curr]+1):
                res = min(res, dfs(jump+1, i + curr))
            return res
        return dfs(0, 0)
        
         0,1,2,3,4,5
        [2,4,1,1,1,1]
        [0,1,0,0,0,0]
        """

        dp = [len(nums)  for i in range(len(nums))]
        dp[0] = 0

        for i in range(1, len(dp)):
            leastJump = len(nums)
            for j in range(i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[j] + 1, dp[i])

        print(dp)
        return dp[-1]


            
