class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        arr = [0]
        def dfs(i, prof):
            if i >= len(nums):
                arr[0] = max(arr[0], prof)
                return

            dfs(i+2, prof + nums[i])
            dfs(i+1, prof)

        dfs(0, 0)
        [0,0,1,1,4]
        """
        dp = [0] * (len(nums) + 2)

        for idx in range(2,len(nums) + 2):
            dp[idx] = max(dp[idx-2] + nums[idx - 2], dp[idx - 1])


        return dp[-1]
