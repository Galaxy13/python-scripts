# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1:
            return list2
        if not list2:
            return list1
        newListNode = ListNode()
        newListNode_link = newListNode
        while list1 and list2:
            if list1.val >= list2.val:
                newListNode.next = list2
                list2 = list2.next
                newListNode = newListNode.next
            elif list2.val > list1.val:
                newListNode.next = list1
                list1 = list1.next
                newListNode = newListNode.next
        if list1:
            newListNode.next = list1
        else:
            newListNode.next = list2
        return newListNode_link.next
