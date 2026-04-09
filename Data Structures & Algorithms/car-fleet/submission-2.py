class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        [(7, 1, 3), (4, 2, 3), (1, 2, 5), (0, 1, 10)]
        """
        n = len(position)
        sortedPS = sorted([[position[i], speed[i]] for i in range(len(position))], key=lambda x: x[0], reverse=True)
        stack = []



        for i in range(n):
            time = (target - sortedPS[i][0]) / sortedPS[i][1]
            if stack:
                if stack[-1] < time:
                    stack.append(time)
            else:
                stack.append(time)
            

        return len(stack)







