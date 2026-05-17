class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray_sum = float("-inf")

        curr_sum = 0
        for num in nums:
            if curr_sum < 0:
                curr_sum = 0

            curr_sum += num
            max_subarray_sum = max(max_subarray_sum, curr_sum)


        return max_subarray_sum

