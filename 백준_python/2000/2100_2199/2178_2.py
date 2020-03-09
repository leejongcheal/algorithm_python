import sys
from sys import stdin
from collections import deque

m, n = [int(x) for x in stdin.readline().split()]  #세로 가로
maze = [[0]*n for i in range(m)]
visit = mat = [[0]*n for i in range(m)]
search = deque()
#미로 받기
for i in range(m):
   str = stdin.readline()
   for j in range(n):
       maze[i][j] = int(str[j])

def find_maze():
    while len(search) > 0:
        x, y = search.popleft()
        if x == m - 1 and y == n - 1:
            print(maze[x][y]-1)
            exit()
        if x > 0 and maze[x-1][y] == 1:
            search.append((x - 1, y))
            maze[x - 1][y] = maze[x][y] + 1
        if x + 1 < m and maze[x + 1][y] == 1:
            search.append((x + 1, y))
            maze[x + 1][y] = maze[x][y] + 1
        if y > 0 and maze[x][y - 1] == 1:
            search.append((x, y - 1))
            maze[x][y - 1] = maze[x][y] + 1
        if y + 1 < n and maze[x][y + 1] == 1:
            search.append((x, y + 1))
            maze[x][y + 1] = maze[x][y] + 1


search.append((0, 0))
maze[0][0] = 2
find_maze()

