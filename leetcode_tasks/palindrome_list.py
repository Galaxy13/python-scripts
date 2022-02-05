# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head) -> bool:
        value_list = []
        while True:
            value_list.append(head.val)
            if not head.next:
                break
            head = head.next
        if len(value_list) == 1:
            return True
        for value_idx in range((len(value_list) // 2) + 1):
            if value_list[value_idx] != value_list[-value_idx - 1]:
                return False
        return True


def isPalindrome(head) -> bool:
    value_list = []
    while True:
        value_list.append(head.val)
        if not head.next:
            break
        head = head.next
    if len(value_list) == 1:
        return True
    for value_idx in range((len(value_list) // 2) + 1):
        if value_list[value_idx] != value_list[-value_idx - 1]:
            return False
    return True


# pol = ListNode(1, ListNode(2, (ListNode(2, (ListNode(1, None))))))
#
# def list_to_listnode(start_list):
#     if not start_list:
#         return None
#     return ListNode(start_list[0], list_to_listnode(start_list[1:]))
#
# pol1 = list_to_listnode([1, 0, 1])
# print(isPalindrome(pol1))
