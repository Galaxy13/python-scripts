class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_depth = 0

    def diameterOfBinaryTree(self, root):
        self.depth(root)
        return self.max_depth

    def depth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)

        self.max_depth = max(self.max_depth, left + right)
        return max(left, right) + 1

print(Solution().diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5)))))

