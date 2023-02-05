import sys
from collections import deque

_, window_len = [int(num) for num in sys.stdin.readline().rstrip('\n').split()]
num_array = [int(num) for num in sys.stdin.readline().rstrip('\n').split()]

def sliding_window_min(arr: list, win_len: int) -> None:
    d = deque()
    init_window = sorted([(arr[index], index) for index in range(win_len)], key= lambda t: t[0], reverse=True)
    for elem in init_window:
        d.append(elem)
    print(d[-1][0])
    for index in range(win_len, len(arr)):
        while d and d[0][0] >= arr[index]:
            d.popleft()
        d.appendleft((arr[index], index))
        while d[-1][1] <= index - win_len:
            d.pop()
        print(d[-1][0])


sliding_window_min(num_array, window_len)
