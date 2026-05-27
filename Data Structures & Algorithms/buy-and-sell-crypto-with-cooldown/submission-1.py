class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        [1, 3, 4, 0, 4]

            -1
          0   -1   
        0  


        """
        memo = {}
        n = len(prices)
        def dfs(i, buying):
            if i >= n:
                return 0

            if (i, buying) in memo:
                return memo[(i, buying)]            
            res = 0
            if buying:
                res = max(dfs(i + 1, False) - prices[i], dfs(i+1, True), res)
            else:
                res =  max(prices[i] + dfs(i + 2, True), dfs(i+1, False), res)
            
            memo[(i, buying)] = res
            return res
        return dfs(0,True)




