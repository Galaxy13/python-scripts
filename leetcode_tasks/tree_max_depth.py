from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        node_queue = deque()
        node_queue.append(root)
        count = 0
        while len(node_queue):
            count += 1
            for node_idx in range(len(node_queue)):
                node = node_queue.popleft()
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
        return count

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        count_left, count_right = 0, 0
        if root.left:
            count_left = self.maxDepth(root.left)
        if root.right:
            count_right = self.maxDepth(root.right)
        return count_left + count_right


# print(Solution().maxDepth(TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))))
# print((Solution().maxDepth(TreeNode(1, None, TreeNode(2, None, None)))))
print(Solution().maxDepth(TreeNode(0)))
print(Solution().diameterOfBinaryTree(TreeNode(4, TreeNode(-7), TreeNode(-3, TreeNode(-9, TreeNode(9, TreeNode(6, TreeNode(0, TreeNode(-1)), TreeNode(6, TreeNode(4)))), TreeNode(-7, TreeNode(-6, TreeNode(5)), TreeNode(-6, TreeNode(9, TreeNode(-2))))), TreeNode(-3, TreeNode(-4))))))