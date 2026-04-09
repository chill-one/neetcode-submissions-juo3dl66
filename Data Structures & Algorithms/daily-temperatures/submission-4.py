class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]

        for curr_day, value in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < value:
                day = stack.pop()
                res[day] = curr_day - day
            stack.append(curr_day)

        return res 