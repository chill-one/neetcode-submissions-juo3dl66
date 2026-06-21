# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        p = k
        res = []
        def dfs(curr):
            nonlocal p
            if not curr:
                return 0
            
            dfs(curr.left)
            p-=1
            if p == 0:
                res.append(curr.val)
            dfs(curr.right)

        dfs(root)

        return res[0]
            