class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        window = [0, 0]

        while window[1] < len(nums) - 1:
            farthest = 0

            for i in range(window[0], window[1] + 1):
                farthest = max(i + nums[i], farthest)

            window[0] = window[1] + 1
            window[1] = farthest
            res += 1

        return res
