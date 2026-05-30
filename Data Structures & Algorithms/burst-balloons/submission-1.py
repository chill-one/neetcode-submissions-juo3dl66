class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        n = len(nums)
        memo = {}
        def dfs(left, right):
            if left + 1 >= right:
                return 0
            
            if (left, right) in memo:
                return memo[(left, right)]

            best = 0
            for k in range(left +1, right):
                coins = nums[left] * nums[k] * nums[right]
                total = dfs(left, k) + coins + dfs(k, right)
                best = max(best, total)
            memo[(left, right)] = best
            return best

        return dfs(0, n-1)