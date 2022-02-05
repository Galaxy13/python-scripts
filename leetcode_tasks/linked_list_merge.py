class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        new_list = ListNode(0)
        new_list_ret = new_list
        while list1 or list2:
            if list1 is None:
                while list2 is not None:
                    new_list.next = list2
                    list2 = list2.next
                    new_list = new_list.next
                break
            if list2 is None:
                while list1 is not None:
                    new_list.next = list1
                    list1 = list1.next
                    new_list = new_list.next
                break
            if list1.val < list2.val:
                new_list.next = list1
                list1 = list1.next
            elif list2.val <= list1.val:
                new_list.next = list2
                list2 = list2.next
            new_list = new_list.next
        return new_list_ret.next


# def list_to_listnode(start_list):
#     if not start_list:
#         return None
#     return ListNode(start_list[0], list_to_listnode(start_list[1:]))
#
# pol1 = list_to_listnode([1, 2, 4])
# pol2 = list_to_listnode([1, 3, 4])
#
# def listnode_to_list(head):
#     if head.next is None:
#         return head.val
#     return [head.val, listnode_to_list(head.next)]
#
