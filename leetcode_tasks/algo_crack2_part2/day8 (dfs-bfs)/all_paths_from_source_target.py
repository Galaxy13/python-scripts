from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        all_ways = []
        def dfs(node=0, way=[]):
            if not graph[node]:
                all_ways.append(way)
                return
            way.append(node)
            for next_node in graph[node]:
                dfs(next_node, way)
        dfs()
        return all_ways

if __name__ == '__main__':
    print(Solution().allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
