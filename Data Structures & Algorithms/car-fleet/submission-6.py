class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """

        [4, 1, 0, 7]. [2, 2, 1, 1]

        [(4, 2), (1, 2), (0, 1), (7, 1)]
        [(7, 1), (4, 2), (1, 2), (0, 1)]



        target = 10.      10 - 7 = 3 / 1 = 3
                          10 - 4 = 6 / 2 = 3
                          10 - 1 = 9 / 2 = 4.
                          10 - 0 = 10 / 1 = 10
        """

        speed_and_pos = [[position[i], speed[i]] for i in range(len(speed))]
        speed_and_pos.sort(key=lambda x : x[0], reverse=True)

        stack = []


        for value in speed_and_pos:
            pos, speed = value
            current_pos = target - pos
            time = current_pos / speed

            if not stack or stack[-1] < time:
                stack.append(time)
    

        return len(stack)