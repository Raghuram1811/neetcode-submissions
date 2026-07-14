# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0

        def explore(node):

            if not node:
                return 0
            left = explore(node.left)
            right = explore(node.right)
            self.res = max(self.res, left + right)

            return max(left, right) + 1
        
        explore(root)

        return self.res
