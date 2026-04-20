# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def sameTree(p, q):
            if not p or not q:
                return p == q

            if p.val != q.val:
                return False

            return sameTree(p.left, q.left) and sameTree(p.right, q.right)


        def dfs(p, q):
            if not p:
                return False

            if sameTree(p, q):
                return True

            left = dfs(p.left, q)
            right = dfs(p.right, q)

            return left or right

            
            
        return dfs(root, subRoot)