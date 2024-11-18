# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return None

        leftTail = self.flatten(root.left)
        rightTail = self.flatten(root.right)

        if root.left:
            leftTail.right = root.right
            root.right = root.left
            root.left = None

        last = leftTail or rightTail or root

        return last
