class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        position = defaultdict(int)

        for p, r in lights:
            position[p - r] += 1
            position[p + r + 1] -= 1


        brightest = 0
        light = 0
        spot = 0
        for p, l in sorted(position.items()):
            brightest += l

            if light < brightest:
                light = brightest
                spot = p

        return spot