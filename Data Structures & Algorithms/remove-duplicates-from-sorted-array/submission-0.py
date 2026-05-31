class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = 0

        for idx in range(1,len(nums)):
            if nums[prev] < nums[idx]:
                nums[prev+1] = nums[idx]
                prev += 1

        return prev +1