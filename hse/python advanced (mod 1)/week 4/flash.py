class Flash:
    def __init__(self, capacity):
        self._capacity = capacity

    def write(self, filesize):
        if filesize <= self._capacity:
            self._capacity -= filesize
        else:
            raise ValueError()