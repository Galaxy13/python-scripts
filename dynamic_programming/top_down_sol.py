class CountDerangementRecTopDown:
    def __init__(self, set_size):
        self.set_size = set_size
        self.sub_sol = [None for x in range(set_size + 1)]

    def count_derangements(self):
        return self.count_derangements_rec(self.set_size)

    def count_derangements_rec(self, n):
        if self.sub_sol[n]:
            return self.sub_sol[n]
        if n == 1:
            return 0
        if n == 2:
            return 1
        result = (n - 1) * (self.count_derangements_rec(n - 1) + self.count_derangements_rec(n - 2))
        self.sub_sol[n] = result
        return result


for i in range(1, 64):
    n = CountDerangementRecTopDown(i).count_derangements()
    print('Derangements in size {} -> {} '.format(i, n))