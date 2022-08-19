from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_Treenode(start_list):
    if not start_list:
        return None
    return TreeNode(start_list[0], list_to_Treenode(start_list[1:]), list_to_Treenode(start_list[2:]))

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        queue1 = deque([root1])
        queue2 = deque([root2])
        while queue1:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            node1.val += node2.val

            if node2.left:
                if node1.left:
                    queue1.append(node1.left)
                    queue2.append(node2.left)
                else:
                    node1.left = node2.left

            if node2.right:
                if node1.right:
                    queue1.append(node1.right)
                    queue2.append(node2.right)
                else:
                    node1.right = node2.right
        return root1


