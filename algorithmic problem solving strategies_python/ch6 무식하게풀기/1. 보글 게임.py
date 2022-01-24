steps = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,1),(1,-1)]
## 완탄이라며 DFS나 BFS를 동반한 완전탐색일 경우 그냥 visit 바로 탑재되어야함
## 탐색의 기본은 한번지난적있는곳을 어떻게 안지나게 할것인가?? 기저사례 + visit 기술

def hasWord(x, y, index):
    global Map, str_len, steps, Word, visit
    if Map[x][y] != Word[index]:
        return 0
    elif Map[x][y] == Word[index] and index == str_len - 1:
        return 1
    else:
        visit[x][y][index] = 1
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and index + 1 < str_len and visit[nx][ny][index + 1] == 0:
                if hasWord(nx, ny, index + 1):
                    return 1
    return 0


for _ in range(int(input())):
    Map = []
    for _ in range(5):
        Map.append(input())
    N = int(input())
    for __ in range(N):
        Word = input()
        str_len = len(Word)
        visit = [[[0]*str_len for _ in range(5)] for ___ in range(5)]
        flag = 0
        for i in range(5):
            for j in range(5):
                if hasWord(i, j, 0):
                    flag = 1
                    break
            if flag == 1:
                break
        if flag:
            print(Word + " YES")
        else:
            print(Word + " NO")