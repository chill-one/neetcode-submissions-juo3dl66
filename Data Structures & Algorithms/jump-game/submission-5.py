class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        """
        def dfs(curr):
            if curr >= len(nums)-1:
                return True
            #jump the amount
            for i in range(1, nums[curr] + 1):
                if dfs(curr + i):
                    return True
            
            return False
        """
        dp = [False for _ in range(len(nums))]
        dp[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            jumps = nums[i]
            for jump in range(1, jumps+1):
                if i + jump >= len(nums) - 1:
                    dp[i] = True
                    break
                else:
                    dp[i] = dp[i + jump] or dp[i]
        return dp[0]

        