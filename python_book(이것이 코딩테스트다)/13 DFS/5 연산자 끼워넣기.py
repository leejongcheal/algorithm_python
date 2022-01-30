"""
itertool의 permutation 을 써도 통과는됌 -> 그러나 거의 한계시간으로 실패한 알고리즘으로보임
BFS를 이용해서 풀수도 있음 (2번째 주석부분) 보면 알겠지만 큐에 oper를 카피하고 해당 명령어를
-1한 리스트값을 q에 넣어서 BFS 돌림 -> 메모리 낭비 + 코딩자체가 까다로움
DFS풀이를 보면 알겠지만
plus -= 1
dfs(i+1,data + L[i])
plus -= 1
처럼 간단한 풀이가 가능함
DFS를 써야하는 경우는 이처럼 visit 함수대신 어떠한 리스트에 대해서 가지고 가야하는 경우
BFS는 q에 계속 리스트를 만들어서 넣어줘야하지만 DFS는 -1 +1 테크닉으로 편하게 풀이가능
특히 순열,조합 느낌나는경우는 DFS풀이를 해줘야함

"""
def dfs(index, now):
    global L, N, plus, minus, mul, div, Max, Min
    if index == 0:
        now = L[index]
    if index == N:
        Max = max(Max, now)
        Min = min(Min, now)
    else:
        if plus > 0:
            plus -= 1
            dfs(index + 1, now + L[index])
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(index + 1, now - L[index])
            minus += 1
        if mul > 0:
            mul -= 1
            dfs(index + 1, now * L[index])
            mul += 1
        if div > 0:
            if L[index] != 0:
                div -= 1
                dfs(index + 1, int(now / L[index]))
                div += 1


N = int(input())
L = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
Max = -1*int(1e10)
Min = int(1e10)
dfs(1, L[0])
print(Max)
print(Min)

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