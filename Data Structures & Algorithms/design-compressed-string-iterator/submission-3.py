class StringIterator:

    def __init__(self, compressedString: str):
        self.str_ = []
        self.count = []

        self.spliting(compressedString)
        self.pos = 0

    def spliting(self, s):
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            else:
                if num:
                    self.count.append(num)
                    num = 0
                self.str_.append(char)
        if num:
            self.count.append(num)

    def next(self) -> str:
        if not self.hasNext():
            return " "
        if self.count[self.pos] <= 0:
            self.pos += 1

        self.count[self.pos] -= 1
        return self.str_[self.pos]
        

    def hasNext(self) -> bool:
        return self.pos <= len(self.str_) 
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
