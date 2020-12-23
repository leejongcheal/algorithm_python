point = input()
cnt = 0
x = int(point[1]) - 1
y = ord(point[0]) - ord('a')
dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [-1, 1, -1, 1, 2, 2, -2, -2]
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < 8 and 0 <= ny < 8:
        cnt += 1
print(cnt)
