# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(root, depth):
            if root.left:
                left_depth = traverse(root.left, depth + 1)
            else:
                left_depth = depth
            if root.right:
                right_depth = traverse(root.right, depth + 1)
            else:
                right_depth = depth
            
            return max(left_depth, right_depth)

        if not root:
            return 0
        
        return traverse(root, 1)