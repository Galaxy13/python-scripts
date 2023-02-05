class Queue:
    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if not self.queue:
            raise IndexError('pop from an empty queue')
        return self.queue.pop(0)

queue = Queue()
try:
    n_experiments = 100
    for elem in range(n_experiments):
        queue.push(elem)
    for elem in range(n_experiments):
        if elem != queue.pop():
            print( f'0\tFailed test #1.{elem}. Please try again!')

except Exception:
    print('0\tFailed test #2. Please try again!')