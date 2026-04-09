class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True


        for idx in range(len(dp)-1, -1 ,-1):
            for word in wordDict:
                if len(word) + idx <= len(s) and s[idx:idx + len(word)] == word:
                    dp[idx] = dp[idx + len(word)]

                if dp[idx]:
                    break

        print(dp)

        return dp[0]
            
            

