from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = ret = ListNode(-301)
        node.next = head
        while node and node.next:
            if node.val != head.val:
                prev = node
                head = head.next
                node = node.next
            else:
                while head and node.val == head.val:
                    head = head.next
                    node = node.next
                node.next = None
                prev.next = head
                node = head
                if head:
                    head = head.next
        return ret.next


if __name__ == "__main__":
    def list_to_listnode(start_list):
        if not start_list:
            return None
        return ListNode(val=start_list[0], next=list_to_listnode(start_list[1:]))


    def listnode_to_list(head):
        if head.next is None:
            return [head.val]
        return [head.val] + listnode_to_list(head.next)


    test_del = Solution().deleteDuplicates(list_to_listnode([1,1,2,2]))
    print(listnode_to_list(test_del))