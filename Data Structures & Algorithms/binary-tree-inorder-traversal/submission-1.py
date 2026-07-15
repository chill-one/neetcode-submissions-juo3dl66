# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        curr = []
        left = self.inorderTraversal(root.left)
        curr.extend(left)
        curr.append(root.val)
        right = self.inorderTraversal(root.right)
        curr.extend(right)

        return curr