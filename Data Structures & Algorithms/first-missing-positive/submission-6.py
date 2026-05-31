class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for idx in range(len(nums)):
            if nums[idx] <= 0 or nums[idx] > len(nums):
                nums[idx] = len(nums) + 1

        for num in nums:
            key = (abs(num) - 1) 

            if key < len(nums):
                nums[key] = -abs(nums[key])

        for idx in range(len(nums)):
            if nums[idx] > 0:
                return idx + 1

        return len(nums) +1


            