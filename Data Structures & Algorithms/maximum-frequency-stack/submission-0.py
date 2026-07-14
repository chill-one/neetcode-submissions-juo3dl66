class FreqStack:

    def __init__(self):
        self.count_stack = defaultdict(int)
        self.stack = defaultdict(list)
        self.max_count = 0

    def push(self, val: int) -> None:
        self.count_stack[val] += 1
        self.max_count = max(self.max_count, self.count_stack[val])
        self.stack[self.count_stack[val]].append(val)

    def pop(self) -> int:
        val = self.stack[self.max_count].pop()
        self.count_stack[val] -= 1
        if len(self.stack[self.max_count]) == 0:
            self.max_count -= 1
        return val


        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()