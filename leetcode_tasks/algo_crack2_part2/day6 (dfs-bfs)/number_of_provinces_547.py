from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count_of_prov = 0

        def bfs(pos):
            queue = [[pos, pos]]
            while queue:
                row, col = queue.pop(0)
                isConnected[row][col] = '#'
                for col in range(len(isConnected)):
                    if isConnected[row][col] == 1:
                        isConnected[row][col] = "#"
                        if row != col:
                            queue.append([col, row])

        for row in range(len(isConnected)):
            if isConnected[row][row] == 1:
                bfs(row)
                count_of_prov += 1
        return count_of_prov


if __name__ == '__main__':
    print(Solution().findCircleNum(isConnected=[[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))