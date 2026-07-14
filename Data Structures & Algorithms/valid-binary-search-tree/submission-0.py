# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check_validity(root, min_value, max_value):

            if not root:
                return True

            if not (root.val > min_value and root.val < max_value):
                return False
            
            left = check_validity(root.left, min_value, root.val)
            right = check_validity(root.right, root.val, max_value)

            return left and right

        if check_validity(root, float("-inf"), float("inf")):
            return True
        
        return False