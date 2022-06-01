
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        path_sum = targetSum - root.val
        if not root.left and not root.right:
            if not path_sum:
                return True
            return False
        if root.left:
            final_sum_left = self.hasPathSum(root.left, path_sum)
            if final_sum_left: return True
        if root.right:
            final_sum_right = self.hasPathSum(root.right, path_sum)
            if final_sum_right: return True
        return False

tree = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7, None, None), TreeNode(2, None, None)), None), TreeNode(8, TreeNode(13, None, None), TreeNode(4, None, TreeNode(1, None, None))))
tree_1 = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
tree_2 = TreeNode(1, None, None)

print(Solution().hasPathSum(tree_2, 1))