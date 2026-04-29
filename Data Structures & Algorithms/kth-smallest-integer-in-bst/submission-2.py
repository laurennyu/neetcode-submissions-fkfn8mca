# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Use inorder traversal
        count = 0
        val = root.val
        def traverse(root):
            nonlocal count, val
            if root.left:
                traverse(root.left)
            if count == k:
                return
            count += 1
            if count == k:
                val = root.val
                return root.val
            if root.right:
                traverse(root.right)
                
        traverse(root)
        return val