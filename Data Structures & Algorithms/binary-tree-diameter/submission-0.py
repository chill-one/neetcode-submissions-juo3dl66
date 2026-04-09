# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = [0]
        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left) 
            right = dfs(curr.right)
            d[0] = max(d[0], left + right)

            return max(left, right) + 1

        dfs(root)
        return d[0]