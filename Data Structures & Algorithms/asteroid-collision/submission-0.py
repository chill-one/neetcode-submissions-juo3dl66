class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        [-1, -2, -3, 4, 5]

        [-5, -5, 5, 5]

        [1, 2. -3]     

        [2] -3
        [-3] 2
        [3] -3
        """
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < abs(asteroid):
                    stack.pop()
                    continue # Keep checking the new stack top
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                # Break or handle the 'incoming destroyed' case
                break

            else:
                stack.append(asteroid)

        return stack
                
                

