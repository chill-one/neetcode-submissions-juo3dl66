# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr, r):
            if not curr:
                return True

            if r[0] >= curr.val or curr.val >= r[1]:
                return False
            
            return dfs(curr.left, [r[0], curr.val]) and dfs(curr.right, [curr.val, r[1]])

        return dfs(root, [float('-inf'), float('inf')])