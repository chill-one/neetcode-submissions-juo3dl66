class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1, 1,  2,  8, 1]
        [48, 48, 24, 6, 1]
        [48, 24, ]
        """
        n = len(nums)
        post_fix = [1] * (n+1)
        pre_fix = [1] * (n+1)


        for i in range(1, n):
            post_fix[i] = post_fix[i-1] * nums[i-1]

        for i in range(n-1, -1, -1):
            pre_fix[i] = pre_fix[i+1] * nums[i]
        
        res = [1] * n
        for i in range(n):
            res[i] = post_fix[i] * pre_fix[i+1]

        return res