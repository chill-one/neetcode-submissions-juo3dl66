class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        """
                []
            [2].    []
        [2 2] [2]. [5]
        """

        def dfs(curr, pos, sum_):
            if sum_ == target:
                res.append(curr)
                return
            elif sum_ > target or pos == len(nums):
                return
            else:
                # keep adding the element at current pos
                curr.append(nums[pos])
                dfs(curr[:], pos, sum_ + nums[pos])
                curr.pop()

                dfs(curr[:], pos+1, sum_)


        
        dfs([], 0, 0)
        return res
