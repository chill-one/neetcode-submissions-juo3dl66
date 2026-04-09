class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)
        dic = {'(': ')', '{':'}', '[':']'}

        for i in range(n):
            if s[i] in dic:
                stack.append(dic[s[i]])
            else:
                if stack and s[i] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0

            
                