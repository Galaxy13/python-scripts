"""
Slow, Fast Pointer
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def listToNode(test_list):
    if not test_list:
        return
    return ListNode(test_list[0], listToNode(test_list[1:]))

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow_p, fast_p = head, head
        while fast_p:
            if fast_p.next:
                slow_p = slow_p.next
            try:
                fast_p = fast_p.next.next
            except AttributeError:
                return slow_p
        return slow_p

print(Solution().middleNode(listToNode([1, 2, 3, 4, 5, 6])))