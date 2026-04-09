# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def rec(root, depth):
            if root == None:
                return depth

            left_depth = rec(root.left, depth + 1) 
            right_depth = rec(root.right, depth + 1) 

            return max(left_depth, right_depth)

        

        return rec(root, 0)
            