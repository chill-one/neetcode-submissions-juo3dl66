class Solution:
    def rob(self, nums: List[int]) -> int:
        

        def houseRob(arr):
            dp = [0] * (len(arr) + 2)

            for i in range(2,len(dp)):
                dp[i] = max(dp[i-2] + arr[i-2], dp[i-1])

            return dp[-1]

        return max(nums[0], houseRob(nums[1:]), houseRob(nums[:-1]))

