class value:
    def __init__(self, value, curr_min):
        self.value = value
        self.curr_min = curr_min

class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if len(self.stack ) == 0:
            self.stack.append(value(val, val))
        else:
            new_min = min(val, self.stack[-1].curr_min)
            self.stack .append(value(val,new_min))

    def pop(self) -> None:
        self.stack .pop()

    def top(self) -> int:
        return self.stack[-1].value

    def getMin(self) -> int:
        return self.stack[-1].curr_min
        
