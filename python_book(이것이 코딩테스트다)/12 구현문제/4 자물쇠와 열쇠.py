import copy
# 90도 회전
def rotation(key):
    M = len(key)
    rotation_key = [[0]*M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            rotation_key[j][M-i-1] = key[i][j]
    return rotation_key


# 0 ~ N - M 이동 총  N - M + 1 번 연산
def check_lock(lock, key,x , y):
    N, M = len(lock), len(key)
    for i in range(N):
        for j in range(N):
            # in에 대해서 하나라도 다른것이 있으면 안맞음
            if x <= i < M + x and y <= j < M + y:
                if lock[i][j] == key[i][j]:
                    return -1
            # out 에 대해서 lock의 홈이 남아있으면 안맞음
            else:
                if lock[i][j] == 0:
                    return -1
    return 1


N, M = map(int, input().split())
lock = []
key = []
for i in range(N):
    lock.append(list(map(int, input().split())))
for i in range(M):
    key.append(list(map(int, input().split())))
# print(lock)
# print(key)
flag = 0
for i in range(4):
    if i != 0:
        key = rotation(key)
    for x in range(-M + 1,N):
        for y in range(-M+1, N):
            if check_lock(lock, key,x ,y) == 1:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 1:
        break
if flag == 1:
    print("true")
else:
    print("false")