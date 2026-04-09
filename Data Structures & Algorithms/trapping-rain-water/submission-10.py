class Solution:
    def trap(self, height: List[int]) -> int:
        res, n = 0, len(height)
        left_max = [0 for _ in range(n)]
        right_max = [0 for _ in range(n)]

        for i in range(n):
            leftMax = 0
            if i > 0:
                leftMax = left_max[i - 1]
            left_max[i] = max(leftMax, height[i])

        for i in range(n-1, -1, -1):
            rightMax = 0
            if i < n-1:
                rightMax = right_max[i + 1]
            right_max[i] = max(rightMax, height[i])

        for i in range(n):
            res += min(left_max[i], right_max[i]) - height[i]

        return res