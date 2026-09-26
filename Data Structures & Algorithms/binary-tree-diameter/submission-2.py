# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.max_depth = 0

        def diameter(node):

            if not node:
                return 0
            
            left = diameter(node.left)
            right = diameter(node.right)

            self.max_depth = max(left + right, self.max_depth)

            return 1 + max(left, right)
        
        diameter(root)

        return self.max_depth
