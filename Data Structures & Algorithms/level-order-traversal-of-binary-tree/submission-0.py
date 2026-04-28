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
        queue = [(root, 1)]

        # BFS
        while len(queue) > 0:
            curr_node, depth = queue.pop(0)
            if depth > len(levels):
                levels.append([curr_node.val])
            else:
                levels[depth - 1].append(curr_node.val)

            if curr_node.left:
                queue.append((curr_node.left, depth + 1))
            if curr_node.right:
                queue.append((curr_node.right, depth + 1))

        return levels