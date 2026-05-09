class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        def dfs(pos, curr):
            res.append(curr)
            for i in range(pos, len(nums)):
                if i > pos and nums[i] == nums[i - 1]:
                    continue

                dfs(i + 1, curr + [nums[i]])

        dfs(0, [])
        return res