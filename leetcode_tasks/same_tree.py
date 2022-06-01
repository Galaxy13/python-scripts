class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        node_queue = [(p, q)]
        while node_queue:
            (p, q) = node_queue.pop()
            if p and q and p.val == q.val:
                node_queue.append((p.left, q.left))
                node_queue.append((p.right, q.right))
            elif p or q:
                return False
        return True
