class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def listToNode(test_list):
    if not test_list:
        return
    return ListNode(test_list[0], listToNode(test_list[1:]))

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = fast = head
        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head



print(Solution().removeNthFromEnd(listToNode([1]), 1))