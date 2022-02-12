from typing import List

from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        N = len(grid)
        M = len(grid[0])
        q = deque()
        index = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == '1':
                    q.append((i, j))
                    grid[i][j] = '0'
                    while q:
                        x, y = q.popleft()
                        for dx, dy in steps:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < N and 0 <= ny < M:
                                if grid[nx][ny] == '1':
                                    grid[nx][ny] = '0'
                                    q.append((nx, ny))
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
