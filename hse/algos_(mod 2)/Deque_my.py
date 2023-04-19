import sys
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

    def clear(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)


class Deque:

    def __init__(self):
        self.front_stack = Stack()
        self.back_stack = Stack()

    def empty(func):
        def wrapped(self, *args):
            if self.front_stack.empty() and self.back_stack.empty():
                print('error')
            else:
                func(self, *args)

        return wrapped

    def push_front(self, element):
        self.front_stack.push(element)
        print('ok', end='\n')

    def front_to_back(self):
        while not self.front_stack.empty():
            self.back_stack.push(self.front_stack.pop())

    def back_to_front(self):
        while not self.back_stack.empty():
            self.front_stack.push(self.back_stack.pop())

    def push_back(self, element):
        self.back_stack.push(element)
        print('ok', end='\n')

    @empty
    def pop_front(self):
        if self.front_stack.empty():
            self.back_to_front()
        print(self.front_stack.pop(), end='\n')

    @empty
    def pop_back(self):
        if self.back_stack.empty():
            self.front_to_back()
        print(self.back_stack.pop(), end='\n')

    @empty
    def front(self):
        if self.front_stack.empty():
            self.back_to_front()
        print(self.front_stack.top(), end='\n')

    @empty
    def back(self):
        if self.back_stack.empty():
            self.front_to_back()
        print(self.back_stack.top(), end='\n')

    def size(self):
        print(len(self.front_stack) + len(self.back_stack), end='\n')

    def clear(self):
        self.back_stack.clear()
        self.front_stack.clear()
        print('ok', end='\n')

    def exit(self):
        print('bye', end='\n')


def deque_process():
    d = Deque()
    command_list = {
        'push_front': d.push_front,
        'push_back': d.push_back,
        'pop_front': d.pop_front,
        'pop_back': d.pop_back,
        'front': d.front,
        'back': d.back,
        'size': d.size,
        'clear': d.clear,
        'exit': d.exit
    }
    for input_line in sys.stdin:
        if input_line == '\n':
            break
        input_line = input_line.rstrip('\n')
        if len(input_line.split()) == 2:
            command, argument = input_line.split()
            command_list[command](argument)
        else:
            command = input_line
            command_list[command]()

deque_process()

