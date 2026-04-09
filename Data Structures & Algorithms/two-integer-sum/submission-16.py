class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        prev = {}
        for i in range(n):
            y = target - nums[i]
            if y in prev:
                return [prev[y], i]
            prev[nums[i]] = i


        return None
