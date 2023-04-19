class ListNode:

    def __init__(self, elem=0):
        self.elem = elem
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self, elem):
        new_elem = ListNode(elem)
        new_elem.prev = self.tail
        if not self.tail is None:
            self.tail.next = new_elem
        if self.head is None:
            self.head = new_elem
        self.tail = new_elem

    def pop_front(self):
        if self.head is None:
            return
        key = self.head.elem
        if not self.head.next is None:
            self.head.next.prev = None
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return key

    def __str__(self):
        i = self.head
        s = []
        while not i is None:
            s.append(i.elem)
            s.append('->')
            i = i.next
        return str(s)


if __name__ == '__main__':
    queue = DoublyLinkedList()
    queue.push_back(7)
    queue.push_back(12)
    queue.push_back(5)
    queue.push_back(32)
    print(queue)
    queue.pop_front()
    print(queue)