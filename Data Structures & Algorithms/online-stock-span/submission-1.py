class StockSpanner:
    """
    span -> some day is the max
            its the number of consecutive days starting fromm that day
            for which the stock price was <= to the price of that day.
    """
    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            p, w = self.stack.pop()
            span += w

        self.stack.append((price, span))
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)