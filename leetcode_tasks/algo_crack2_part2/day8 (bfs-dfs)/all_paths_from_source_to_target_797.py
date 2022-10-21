from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        fin_list = []
        def dfs(node, path=[0]):
            if node == len(graph) - 1:
                fin_list.append(path)
                return
            for new_node in graph[node]:
                dfs(new_node, path + [new_node])

        dfs(0)
        return fin_list

if __name__ == '__main__':
    print(Solution().allPathsSourceTarget([[4,3,1],[3,2,4],[],[4],[]]))