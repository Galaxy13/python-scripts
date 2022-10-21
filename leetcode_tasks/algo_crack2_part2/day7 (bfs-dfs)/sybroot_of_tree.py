from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        if not sub_root: return True
        if not root: return False

        if self.is_same_tree(root, sub_root):
            return True

        return self.isSubtree(root.left, sub_root) or self.isSubtree(root.right, sub_root)

    def is_same_tree(self, s, q):
        if not s and not q: return True
        if s and q and s.val == q.val:
            return (self.is_same_tree(s.left, q.left) and self.is_same_tree(s.right, q.right))

        return False

def listToTreeNode(start_list):
    if not start_list:
        return None
    return TreeNode(start_list[0], listToTreeNode(start_list[1:]), listToTreeNode(start_list[2:]))

if __name__ == '__main__':
    print(Solution().isSubtree(TreeNode(3, ), listToTreeNode([4,1,2])))
