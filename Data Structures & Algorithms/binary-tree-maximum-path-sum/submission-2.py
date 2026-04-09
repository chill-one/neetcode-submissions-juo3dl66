# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(curr):
            if not curr:
                return 0

            #Gets rid of the negativ value
            left_value, right_value = max(dfs(curr.left),0), max(dfs(curr.right),0)
            value = max(left_value, right_value) + curr.val
            res[0] = max(res[0], left_value + right_value + curr.val)

            return value
        dfs(root)
        return res[0]



            

            