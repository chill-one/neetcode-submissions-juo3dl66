class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        1 2 4 6
        48 24 12 8

        """

        pre_sum = 1
        res = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            res[i] = pre_sum
            pre_sum *= nums[i]

        post_sum = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post_sum
            post_sum *= nums[i]

        return res
            