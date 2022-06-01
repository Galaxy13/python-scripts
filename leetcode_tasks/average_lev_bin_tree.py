# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        node_queue = [root]
        average_sum_list = []
        while len(node_queue):
            count = 0
            value = 0
            for queue_idx in range(len(node_queue)):
                curr_node = node_queue.pop(0)
                value += curr_node.val
                count += 1
                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
            average_sum_list.append(value/count)
        return average_sum_list


tree = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))

sol = Solution()
print(sol.averageOfLevels(tree))

