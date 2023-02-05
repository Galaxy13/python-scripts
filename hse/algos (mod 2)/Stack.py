class Stack:

    def __init__(self, init_stack=[]):
        self.stack = init_stack

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


class MaxStack:

    def __init__(self):
        self.stack = Stack()
        self.max_stack = Stack()

    def push(self, element):
        self.stack.push(element)
        cur_max = self.max_stack.top() if not self.max_stack.empty() else element
        self.max_stack.push(max(cur_max, element))

    def pop(self):
        self.max_stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack.pop()

    def max(self):
        return self.max_stack.top()

    def __str__(self):
        return "stack: " + str(self.stack) + '\nmax_stack: ' + str(self.max_stack)


if __name__ == '__main__':
    s = Stack([1, 3, 5])
    s.push(7)
    print(s)
    print(s.pop())
    print(s.top())
    print(s)
