class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(pos, curr, sum_):
            if sum_ == target:
                res.append(curr)
                return

            elif sum_ > target or len(candidates) == pos:
                return
            else:
                # go through every candidates and skip duplicates
                for i in range(pos, len(candidates)):
                    if i > pos and candidates[i] == candidates[i - 1]:
                        continue
                    # dfs with the current candidate included 
                    dfs(i + 1,  curr + [candidates[i]], sum_ + candidates[i])

                    

        dfs(0, [], 0)
        return res

