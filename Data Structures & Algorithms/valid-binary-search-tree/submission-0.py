# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr, interval=[float("-infinity"), float("infinity")]):
            if curr == None:
                return True

            if (curr.val > interval[0] and curr.val < interval[1]):
                return dfs(curr.left, [interval[0], curr.val]) and dfs(curr.right, [curr.val, interval[1]])
            else:
                return False

        return dfs(root)
                
            
            

        