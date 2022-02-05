# Definition for singly-linked list.
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
        temp_list = []
        if not head:
            return head
        temp_node = head
        while temp_node:
            temp_list.append(temp_node.val)
            temp_node = temp_node.next
        temp_list.reverse()
        return list_to_listnode(temp_list)


pol1 = list_to_listnode([1, 2, 3, 4, 5])
sol = Solution()
print(sol.reverseList(pol1))
