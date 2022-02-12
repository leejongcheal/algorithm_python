from typing import List

from collections import deque


class Solution:
    def dfs(self, grid: List[List[str]], x:int, y:int) -> None:
        steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] == "1":
                    grid[nx][ny] = '0'
                    self.dfs(grid, nx, ny)

    def numIslands(self, grid: List[List[str]]) -> int:
        N = len(grid)
        M = len(grid[0])
        index = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    index += 1
        return index


# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(Solution().numIslands(grid))
