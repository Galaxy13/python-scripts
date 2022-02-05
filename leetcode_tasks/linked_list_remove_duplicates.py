# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    if not head:
        return head
    temp_node = head
    while temp_node:
        if temp_node.next:
            if temp_node.val == temp_node.next.val:
                temp_node.next = temp_node.next.next
                continue
        temp_node = temp_node.next
    return head

def list_to_listnode(start_list):
    if not start_list:
        return None
    return ListNode(start_list[0], list_to_listnode(start_list[1:]))

pol1 = (list_to_listnode([1, 1, 2, 3]))

def listnode_to_list(head):
    if head.next is None:
        return head.val
    return [head.val, listnode_to_list(head.next)]


print(deleteDuplicates(pol1))

# print(listnode_to_list(target_obj))