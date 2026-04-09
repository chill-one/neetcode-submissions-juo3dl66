class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        1 , 2, 4, 6
        """
        N = len(nums)
        res = [1 for i in range(N)]

        prefix = 1
        for idx in range(N):
            res[idx] = prefix
            prefix *= nums[idx]

        postfix = 1
        for idx in range(N-1 , -1, -1):
            res[idx] *= postfix
            postfix *= nums[idx]

        return res

        
