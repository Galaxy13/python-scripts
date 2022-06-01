class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode):
        if not root:
            return 0
        node_queue = [root]
        count = 0
        while len(node_queue):
            count += 1
            for queue_idx in range(len(node_queue)):
                curr_node = node_queue.pop(0)
                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
                if not curr_node.right and not curr_node.left:
                    return count

tree = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))
tree1 = None

sol = Solution()
print(sol.minDepth(tree1))