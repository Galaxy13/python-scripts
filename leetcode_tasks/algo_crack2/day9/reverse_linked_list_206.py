import dis

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_listnode(start_list):
    if not start_list:
        return None
    return ListNode(start_list[0], list_to_listnode(start_list[1:]))


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        head_reverse = head.next
        head.next = None

        def recur_reverse(head_prev, head_next):
            init_next = head_next.next
            head_next.next = head_prev
            if init_next:
                return recur_reverse(head_next, init_next)
            else:
                return head_next

        return recur_reverse(head, head_reverse)


class Solution_iter:
    def reverseListiter(self, head):
        head_prev = None
        head_next = head
        while head_next:
            init_next = head_next.next
            head_next.next = head_prev
            head_prev = head_next
            head_next = init_next
        return head_prev


dis.dis(Solution().reverseList)
dis.dis(Solution_iter().reverseListiter)