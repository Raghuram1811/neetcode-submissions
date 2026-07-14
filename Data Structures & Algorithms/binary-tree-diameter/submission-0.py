# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.max_path = 0

        def explore(node):
            if not node:
                return 0
            
            left = explore(node.left)
            right = explore(node.right)

            self.max_path = max(self.max_path, left + right)

            return 1 + max(left, right)
        
        explore(root)

        return self.max_path