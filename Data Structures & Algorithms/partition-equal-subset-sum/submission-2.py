class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s // 2

        def dfs(i, sum1):
            if target == sum1:
                return True
            if sum1 > target:
                return False
            if i == len(nums):
                return sum1 == target

            if dfs(i+1, sum1 + nums[i]) or dfs(i+1, sum1):
                return True

            return False


        return dfs(0, 0)
        """
        n = len(nums)
        dp = [0] * (n+1)

        for i in range(1, len(dp)):
            dp[i] = dp[i - 1]
        """
            