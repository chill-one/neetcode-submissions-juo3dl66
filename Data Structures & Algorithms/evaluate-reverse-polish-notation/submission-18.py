class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for char in tokens:
            if char == "+":
                first, second = stack.pop(), stack.pop()
                stack.append(first + second)
            elif char == "*":
                first, second = stack.pop(), stack.pop()
                stack.append(first * second)
            elif char == "-":
                second, first = stack.pop(), stack.pop()
                stack.append(first - second)
            elif char == "/":
                second, first = stack.pop(), stack.pop()
                stack.append(int(first/second))
            else:
                stack.append(int(char))
        
        return stack[-1]