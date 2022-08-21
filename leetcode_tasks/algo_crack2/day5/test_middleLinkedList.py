from middle_of_linked_list_876 import Solution as s
from middle_of_linked_list_876 import ListNode

sol = s().middleNode


def listToNode(test_list):
    if not test_list:
        return
    return ListNode(test_list[0], listToNode(test_list[1:]))

#
# def test_middleLinkedLIst():
#     assert sol(listToNode([1, 2, 3, 4, 5])) == ListNode(3, ListNode(4, (ListNode(5))))

print(sol(listToNode([1, 2, 3, 4, 5])))
