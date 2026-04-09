# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isB = [True]
        def dfs(curr):
            if not curr:
                return 1

            left = dfs(curr.left)
            right = dfs(curr.right)

            diff = abs(left - right)
            if diff > 1:
                isB[0] = False

            return max(left, right) + 1
        dfs(root)
        return isB[0]
