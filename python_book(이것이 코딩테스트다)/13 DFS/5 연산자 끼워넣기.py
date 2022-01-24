from collections import deque


def new_oper(oper, index):
    s = [0] * 4
    for i in range(4):
        s[i] = oper[i]
    s[index] -= 1
    return s


def BFS(N, A, oper):
    result = []
    # 계산값 /index위치/ 현재 oper 리스트
    q = deque()
    q.append((A[0], 1, oper))
    while q:
        res, index, op = q.popleft()
        if index == N:
            result.append(res)
            continue
        a, b, c, d = op[0], op[1], op[2], op[3]
        if a != 0:
            q.append((res + A[index], index + 1, [a - 1, b, c, d]))
        if b != 0:
            q.append((res - A[index], index + 1, [a, b - 1, c, d]))
        if c != 0:
            q.append((res * A[index], index + 1, [a, b, c - 1, d]))
        if d != 0:
            if res < 0 and A[index] > 0:
                q.append((-1 * ((-1 * res) // A[index]), index + 1, [a, b, c, d - 1]))
            elif res > 0 and A[index] < 0:
                q.append((-1 * (res // (-1 * A[index])), index + 1, [a, b, c, d - 1]))
            else:
                q.append((res // A[index], index + 1, [a, b, c, d - 1]))
    return result


N = int(input())
A = list(map(int, input().split()))
# + - * % 순서
oper = list(map(int, input().split()))
result = BFS(N, A, oper)
# print(len(result))
print(max(result), min(result))

### 람다 사용 BFS약간의 응용 + 계산을 함수로 뺴서 풀이 -> 깔끔
# def deep_copy(L):
#     copy = []
#     for i in L:
#         copy.append(i)
#     return copy
#
#
# def calculate(x, y, index):
#     if index == 0:
#         return x + y
#     elif index == 1:
#         return x - y
#     elif index == 2:
#         return x * y
#     elif index == 3:
#         if x * y < 0:
#             return (abs(x) // abs(y)) * (-1)
#         return x // y
#
#
# N = int(input())
# L = list(map(int, input().split()))
# oper = list(map(int, input().split()))
# q = []
# value = L[0]
# q.append((oper, value))
# for index in range(1, len(L)):
#     new = []
#     while q:
#         oper, value = q.pop()
#         for i in range(4):
#             if oper[i] != 0:
#                 oper[i] -= 1
#                 new_oper = deep_copy(oper)
#                 new.append((new_oper, calculate(value, L[index], i)))
#                 oper[i] += 1
#     q = new
# q.sort(key=lambda x: x[1])
# print(q[-1][1])
# print(q[0][1])