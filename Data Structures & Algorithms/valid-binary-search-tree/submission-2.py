class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidMinMax(root):
            if not root:
                return True, float('inf'), float('-inf')

            left_valid, left_min, left_max = isValidMinMax(root.left)
            right_valid, right_min, right_max = isValidMinMax(root.right)

            if left_valid and right_valid and (left_max < root.val < right_min):
                return True, min(left_min, root.val), max(right_max, root.val)

            return False, float('-inf'), float('inf')

        return isValidMinMax(root)[0]