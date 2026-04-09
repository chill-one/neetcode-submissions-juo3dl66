class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        1 , 2, 4, 6
        """
        N = len(nums)
        prefix = [1 for i in range(N)]

        for idx in range(N):
            left = 1
            if idx - 1 >= 0:
                left = prefix[idx - 1]

            prefix[idx] = nums[idx] * left

        postfix = 1
        for idx in range(N-1 , -1, -1):
            left, right = 1, 1
            if idx - 1 >= 0:
                left = prefix[idx - 1]
            prefix[idx] = left * postfix
            postfix = nums[idx] * postfix

        return prefix

        
