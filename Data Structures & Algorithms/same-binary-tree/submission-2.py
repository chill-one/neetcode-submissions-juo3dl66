# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(curr1, curr2):
            if not curr1 or not curr2:
                return curr1 == curr2

            if curr1.val != curr2.val:
                return False

            left = dfs(curr1.left, curr2.left) 
            right = dfs(curr1.right, curr2.right)

            return left and right
        return dfs(p, q)