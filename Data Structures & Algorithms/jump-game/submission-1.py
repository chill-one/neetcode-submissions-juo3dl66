class Solution:
    def canJump(self, nums: List[int]) -> bool:
        post = len(nums) - 1

        for idx in range(len(nums)-2, -1, -1):
            if nums[idx] + idx >= post:
                post = idx

        
        return True if post == 0 else False
        