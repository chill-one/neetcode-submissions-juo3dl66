# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(curr1, curr2):
            # If one of the node is None
            if not curr1 or not curr2:
                # True if both are none else False 
                return curr1 == curr2
            
            #Values are different
            if curr1.val != curr2.val:
                return False

            left = dfs(curr1.left, curr2.left) 
            right = dfs(curr1.right, curr2.right)

            #Both have to be the same value 
            return left and right
        return dfs(p, q)