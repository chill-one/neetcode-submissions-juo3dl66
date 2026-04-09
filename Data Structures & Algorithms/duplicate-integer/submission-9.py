class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        set_ = set()
        for i in range(n):
            if nums[i] in set_:
                return True
            set_.add(nums[i])


        return False