class Stack:

    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return str(self.stack)


class Queue:

    def __init__(self, max_len=100):
        self.head = self.tail = 0
        self.queue = [0] * max_len
        self.max_len = max_len

    def enqueue(self, element):
        self.queue[self.tail] = element
        self.tail = (self.tail + 1) % self.max_len

    def deque(self):
        res = self.queue[self.head]
        self.head = (self.head + 1) % self.max_len
        return res

    def empty(self):
        return self.head == self.tail

    def __str__(self):
        i = self.head
        q = []
        while i < self.tail:
            q.append(self.queue[i])
            i = (i + 1) % self.max_len
        return str(q)


class TwoStacksQueue:

    def __init__(self):
        self.to_enqueue = Stack()
        self.to_deque = Stack()

    def enqueue(self, element):
        self.to_enqueue.push(element)

    def deque(self):
        if self.to_deque.empty():
            while not self.to_enqueue.empty():
                self.to_deque.push(self.to_enqueue.pop())
        return self.to_deque.pop()

    def empty(self):
        return self.to_enqueue.empty() and self.to_deque.empty()

    def __str__(self):
        return str(eval(str(self.to_deque))[::-1] + eval(str(self.to_enqueue)))


if __name__ == '__main__':
    q = TwoStacksQueue()
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(5)
    q.enqueue(12)
    print(q)
    q.deque()
    q.deque()
    print(q)
