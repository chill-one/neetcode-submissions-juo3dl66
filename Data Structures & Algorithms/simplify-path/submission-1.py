class Solution:
    def simplifyPath(self, path: str) -> str:
        curr = path.split("/")
        print(curr)
        stack = []

        for value in curr:
            if len(value) == 0 or value == ".":
                continue

            if value == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(value)

        res = "/" + "/".join(stack)
        return res