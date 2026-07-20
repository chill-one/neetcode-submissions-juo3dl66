class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for string in path.split('/'):
            if len(string) == 0:
                continue

            if string == "..":
                if stack:
                    stack.pop()
            elif string != ".":
                stack.append(string)


        return "/" + "/".join(stack)