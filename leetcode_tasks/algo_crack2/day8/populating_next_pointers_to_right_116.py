# Definition for a Node.
import collections


class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return None
        queuer = [root]
        level_num = 1
        counter = 1
        while queuer:
            node = queuer.pop(0)
            if node.left:
                queuer.append(node.left)
                queuer.append(node.right)
            if counter < level_num:
                counter += 1
                node.next = queuer[0]
            else:
                node.next = None
                counter = 1
                level_num *= 2
        return root

node = Node(0, Node(1, Node(3, None, None), Node(4, None, None)), Node(2, Node(5, None, None), Node(6, None, None)))

Solution().connect(node)
