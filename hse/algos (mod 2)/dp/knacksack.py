import math


def knapsack_recursive(W, V, C):

    def K(i, j):
        if i == 0:
            return 0 if j >= 0 else -math.inf
        return max(K(i-1, j), K(i - 1, j - W[i - 1]) + V[i - 1])
    return K(len(W), C)

def knapsack_dynamic(W,V,C):
    n = len(W)
    tbl = [[0] * (C + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(C + 1):
            tbl[i][j] = tbl[i-1][j]
            if j >= W[i-1]:
                tbl[i][j] = max(tbl[i][j], tbl[i - 1][j - W[i-1]] + V[i - 1])
    return tbl[-1][-1]