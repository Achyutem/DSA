# https://leetcode.com/problems/binary-tree-inorder-traversal/


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []

        def traverse(node):
            if not node:
                return

            traverse(node.left)
            stack.append(node.val)
            traverse(node.right)

        traverse(root)
        return stack
