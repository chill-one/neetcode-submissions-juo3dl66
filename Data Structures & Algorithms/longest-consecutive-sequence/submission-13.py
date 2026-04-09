class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_ = set(nums)
        
        res = 0
        for num in nums:
            curr_val = 0
            pos_val = num 
            while pos_val in set_:
                curr_val += 1
                pos_val += 1

            neg_val = num - 1
            while neg_val in set_:
                curr_val += 1
                neg_val -= 1
            res = max(curr_val, res)


        return res
            
