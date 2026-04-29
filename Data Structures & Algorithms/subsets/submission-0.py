class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        1 2 3

        """
        res = []

        def backTrack(i, curr_path):
            if i >= len(nums):
                res.append(curr_path)
                return

            backTrack(i + 1, curr_path[:])
            curr_path.append(nums[i])
            backTrack(i + 1, curr_path)

        backTrack(0, [])
        return res
