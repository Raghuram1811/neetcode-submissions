# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        output = []
        self.inOrder(root, output, k)
        return output[k-1]
        
    
    def inOrder(self, root: Optional[TreeNode], output: List[int], k:int) -> List[int]:

        if root and len(output)<=k:
            self.inOrder(root.left, output, k)
            heapq.heappush(output, root.val)
            self.inOrder(root.right, output, k)