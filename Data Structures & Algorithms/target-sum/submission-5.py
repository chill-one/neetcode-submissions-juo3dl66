class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        m = sum(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(n):
            temp = [defaultdict(int) for _ in range(n+1)]
            for curr_sum, count in dp[i].items():
                temp[i+1][curr_sum + nums[i]] += count
                temp[i+1][curr_sum - nums[i]] += count
            dp = temp.copy()

        return dp[n][target]


            