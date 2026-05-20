class Solution:
    def checkValidString(self, s: str) -> bool:
        openStack = []
        starStack = []

        for idx in range(len(s)):
            char = s[idx]
            if char == ')':
                if openStack:
                    openStack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False
            elif char == '*':
                starStack.append(idx)
            else:
                openStack.append(idx)

        while openStack and starStack:
            #The star must appear AFTER the '(' to close it
            if openStack[-1] < starStack[-1]:
                openStack.pop()
                starStack.pop()
            else:
                #The '(' is to the right of the last available '*
                break

        return len(openStack) == 0

                

        

                

            
