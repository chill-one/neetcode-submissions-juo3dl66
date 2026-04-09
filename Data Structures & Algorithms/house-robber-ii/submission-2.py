class Solution:
    def rob(self, nums: List[int]) -> int:
        def robbing(arr):
            rob1, rob2 = 0, 0

            for n in arr:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp

            return rob2

        return max(nums[0], robbing(nums[1:]), robbing(nums[:-1]))
        