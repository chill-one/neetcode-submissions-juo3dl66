class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        keep picking the current one
        dont pick this one
        """
        memo = {}
        def dfs(i,total):
            if i >= len(coins) or total > amount:
                return 0
            if (i, total) in memo:
                return memo[(i, total)]

            if total == amount:
                return 1

            res = dfs(i, total + coins[i]) + dfs(i+1, total)
            
            memo[(i, total)] = res
            return res
        return dfs(0, 0)
            

            