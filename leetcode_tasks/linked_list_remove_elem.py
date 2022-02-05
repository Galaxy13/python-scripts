# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head, val: int):
        if head is None:
            return None
        if head.val == val:
            head = head.next
        return ListNode(head.val, self.removeElements(head.next, val))


def removeElements(head, val: int):
    if head is None:
        return None
    if head.val == val:
        head = head.next
    return ListNode(head.val, removeElements(head.next, val))


# pol = ListNode(1, ListNode(2, (ListNode(2, (ListNode(1, None))))))

def list_to_listnode(start_list):
    if not start_list:
        return None
    return ListNode(start_list[0], list_to_listnode(start_list[1:]))

pol1 = (list_to_listnode([7, 7, 7, 7]))

print(removeElements(pol1, 7))
