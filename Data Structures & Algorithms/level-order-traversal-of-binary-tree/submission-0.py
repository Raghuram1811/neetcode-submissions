# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        levels = []

        def helper(root: TreeNode, level: int):

            if len(levels) == level:
                levels.append([])
            
            levels[level].append(root.val)

            if root.left:
                helper(root.left, level+1)

            if root.right:
                helper(root.right, level+1)


        helper(root, 0)
        return levels