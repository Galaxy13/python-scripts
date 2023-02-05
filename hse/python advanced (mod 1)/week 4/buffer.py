class Buffer:
    def __init__(self, maxsize):
        self._buffer_size = maxsize
        self._buffer = []

    def add(self, *elements):
        if len(self._buffer) + len(elements) >= self._buffer_size:
            prev_len = len(self._buffer)
            self._buffer.extend(elements[:self._buffer_size - prev_len])
            print(sum(self._buffer))
            self._buffer.clear()
            self.add(*elements[self._buffer_size - prev_len:])
        else:
            self._buffer.extend(elements)
            return

    def get_current_part(self):
        return self._buffer

buffer = Buffer(5)
buffer.add(*list(range(13)))
buffer.add(*list(range(3)))
buffer.add(*list(range(13, 20)))
buffer.add(*list(range(3, -20, -2)))
buffer.add(*list(range(100, 105)))
print(buffer.get_current_part())