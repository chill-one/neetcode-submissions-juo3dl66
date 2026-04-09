class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        -1 -2 -3 2 2
        
        """
        
        for num in nums:
            k = abs(num) - 1
            if nums[k] < 0:
                return k + 1
            nums[k] = -abs(nums[k])
        return len(nums) + 1