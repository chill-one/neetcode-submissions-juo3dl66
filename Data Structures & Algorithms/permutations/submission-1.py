class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
                 []
            [1,]1     []1
    [1, 2,]2     [1,]2
[1,2,3]3[1, 2]3 [1,3]3 [1,]3
        """
        res = []

        def dfs(curr, exclude):
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for i in range(len(exclude)):
                if not exclude[i]:
                    curr.append(nums[i])
                    exclude[i] = True
                    dfs(curr, exclude)

                    exclude[i] = False
                    curr.pop()
        dfs([], [False] * (len(nums)))
        return res


