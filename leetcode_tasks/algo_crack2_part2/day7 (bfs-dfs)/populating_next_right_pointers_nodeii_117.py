# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return root
        queue = [root]
        queue_next = []
        while queue:
            node = queue.pop(0)
            if node.left: queue_next.append(node.left)
            if node.right: queue_next.append(node.right)
            if queue:
                node.next = queue[0]
            else:
                node.next = None
                queue = [node for node in queue_next]
                queue_next = list()
        return root


def list_to_listnode(start_list):
    if not start_list:
        return None
    return Node(start_list[0], list_to_listnode(start_list[1:]), list_to_listnode(start_list[2:]))


if __name__ == '__main__':
    print(Solution().connect(list_to_listnode([1, 2, 3, 4, 5, None, 7])))
