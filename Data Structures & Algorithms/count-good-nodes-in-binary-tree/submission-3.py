# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count = [0]
        def dfs(curr, prev_max):
            if not curr:
                return 0;

            curr_max = max(prev_max, curr.val) 
            if prev_max <= curr.val:
                count[0] += 1
            
            dfs(curr.left, curr_max)
            dfs(curr.right, curr_max)

        dfs(root, -1000)
        return count[0]

