class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            length = len(stack)

            match char:
                case '+':
                    stack.append(int(stack.pop() + stack.pop()))
                case '-':
                    num1 = stack.pop()
                    stack.append(int(stack.pop() - num1))
                case '*':
                    stack.append(int(stack.pop() * stack.pop()))
                case '/':
                    num1 = stack.pop()
                    stack.append(int(stack.pop() / num1))
                case _:
                    stack.append(int(char))

        return int(stack[0])
                    