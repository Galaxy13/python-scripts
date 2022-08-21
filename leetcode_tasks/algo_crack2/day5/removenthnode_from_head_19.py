# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow_p = fast_p = head
        for _ in range(n):
            fast_p = fast_p.next

        if not fast_p:
            return head.next

        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next

        slow_p.next = slow_p.next.next
        return head