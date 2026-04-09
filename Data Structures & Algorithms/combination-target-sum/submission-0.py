class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def decsionTree(idx, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if idx >= len(nums) or total > target:
                return

            cur.append(nums[idx])
            decsionTree(idx, cur, total + nums[idx])
            cur.pop()
            decsionTree(idx + 1, cur, total)

        decsionTree(0,[],0)
        return res
