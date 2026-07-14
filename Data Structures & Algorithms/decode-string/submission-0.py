class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        string = ""
        res = ""
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '[':
                stack.append((num, "".join(string)))
                string = ""
                num = 0
            elif char == ']':
                old_num, old_string = stack.pop()
                string = old_string + ("".join(string) * old_num)
            else:
                string += char

        return string