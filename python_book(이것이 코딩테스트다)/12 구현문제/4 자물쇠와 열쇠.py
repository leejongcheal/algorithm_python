def rotate(key, M):
    copy = [[0]*M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            copy[j][M-1-i] = key[i][j]
    return copy


def deep_copy(N, lock):
    copy = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            copy[i][j] = lock[i][j]
    return copy


def check(key, lock, N, M, mx, my):
    copy = deep_copy(N,lock)
    for i in range(M):
        for j in range(M):
            if 0 <= i + mx < N and 0 <= j + my < N:
                copy[i+mx][j + my] += key[i][j]
    for i in range(N):
        for j in range(N):
            if copy[i][j] != 1:
                return 0
    return 1


def solution(key, lock):
    M = len(key)
    N = len(lock)
    for r in range(4):
        if r != 0 :
            key = rotate(key, M)
        for i in range(-(M-1), N):
            for j in range(-(M-1), N):
                if check(key, lock, N, M, i, j):
                    return True
    return False


key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]
print(solution(key, lock))