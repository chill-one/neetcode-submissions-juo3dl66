class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        3
               (
            ((  ()
        (((  (()
(((( ((())) (()( (())

        """
        res = []

        def dfs(curr, opening, closing):
            
            if opening == 0 and closing == 0:
                res.append("".join(curr))
                return
            else:
                if opening > 0:
                    dfs(curr + ["("], opening - 1, closing)

                if closing > opening:
                    dfs(curr + [")"], opening, closing - 1)

        dfs([], n, n)
        return res

            