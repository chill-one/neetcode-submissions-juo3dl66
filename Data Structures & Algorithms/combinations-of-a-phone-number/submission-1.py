class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        map = {
            "2": "abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        comb = []
        for num in digits:
            comb.append(map[num])

        res = []
        def dfs(i,curr):
            if len(curr) == len(digits):
                res.append("".join(curr))
                return
            if i >= len(comb):
                return
            
            for j in range(len(comb[i])):
                curr.append(comb[i][j])
                dfs(i+1, curr[:])
                curr.pop()

        dfs(0, [])
        return res
