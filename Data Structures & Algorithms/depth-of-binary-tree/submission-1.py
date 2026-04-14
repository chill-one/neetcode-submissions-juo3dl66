# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(curr):
            if not curr:
                return 0

            curr_depth = max(dfs(curr.left) + 1, dfs(curr.right) + 1)
            return curr_depth



        return dfs(root)