import math


def tj_dynamic(L, W):
    n = len(W)
    tbl = [math.inf] * (n + 1)
    splt = [0] * (n + 1)
    tbl[0] = 0
    for i in range(1, n + 1):
        length = -1
        for j in range(i-1, -1, -1):
            length += 1 + len(W[j])
            if length > L:
                P = math.inf
            else:
                P = (L - length) ** 3
            if tbl[j] + P < tbl[i]:
                tbl[i] = tbl[j] + P
                splt[i] = j
    splt_index = n - 1
    ret_list = []
    prev = splt_index + 1
    splt = splt[1:]
    while 1:
        if splt_index > 0:
            ret_list.append(W[splt_index:prev])
            prev = splt_index
            splt_index = splt[splt_index - 1]
        else:
            ret_list.append(W[0:prev])
            return ret_list

example = ['jars', 'jaws', 'joke', 'jury', 'juxtaposition']

print(tj_dynamic(15, example))