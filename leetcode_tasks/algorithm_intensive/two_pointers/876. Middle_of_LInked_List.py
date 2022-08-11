class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow_p, fast_p = head, head.next
        indicator = True
        while fast_p:
            if indicator:
                slow_p = slow_p.next
                indicator = False
            else:
                indicator = True
            fast_p = fast_p.next
        return slow_p

def listToNode(test_list):
    if not test_list:
        return
    return ListNode(test_list[0], listToNode(test_list[1:]))

print(Solution().middleNode(listToNode([1, 2])))