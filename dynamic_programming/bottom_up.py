class CountDerangementRecBottomUpOpt:
    def __init__(self, set_size):
        self.set_size = set_size
        self.sol_n, sol_n1, sol_n2 = 0, 1, 0
        for n in range(1, set_size + 1):
            if n == 1:
                self.sol_n = 0
            elif n == 2:
                self.sol_n = 1
            else:
                self.sol_n = (n - 1) * (sol_n1 + sol_n2)
            sol_n2 = sol_n1
            sol_n1 = self.sol_n

    def count_derangements(self):
        return self.sol_n

    # def count_derangements_rec(self, n):
    #     if self.sub_sol[n]:
    #         return self.sub_sol[n]
    #     result = (n - 1) * (self.count_derangements_rec(n - 1) + self.count_derangements_rec(n - 2))
    #     self.sub_sol[n] = result
    #     return result


for i in range(1, 64):
    n = CountDerangementRecBottomUpOpt(i).count_derangements()
    print('Derangements in size {} -> {} '.format(i, n))