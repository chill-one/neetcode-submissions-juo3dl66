class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        negative, zero -> make them a 1
        [-1, -1,-1,-2,3,4] 5
         0 1 2 3

        [0]1
        pos = -1
        [-1,-2,-3,-4] len(arry) + 1

        [-1, -2, 4] 3
        [-1, -2, -4, -5, -6, -3, 1]
        """
        new_nums = [len(nums) + 1 if num <= 0 else num for num in nums]
        for idx, num in enumerate(new_nums): 
            key = abs(num) - 1
            if 0 <= key < len(nums):
                new_nums[key] = -abs(new_nums[key])

        for idx, num in enumerate(new_nums):
            if num > 0:
                return idx + 1


        return len(nums) + 1