# https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3
def solution(n, arr1, arr2):
    answer = []
    L1 = [[0]*n for _ in range(n)]
    L2 = [[0]*n for _ in range(n)]
    for i, val in enumerate(arr1):
        r = val
        for j in range(n):
            r, c = r//2, r%2
            L1[i][n-1-j] = c
    for i, val in enumerate(arr2):
        r = val
        for j in range(n):
            r, c = r // 2, r % 2
            L2[i][n-1-j] = c
    for i in range(n):
        for j in range(n):
            if L2[i][j] == 1:
                L1[i][j] = 1
    for i in range(n):
        temp = ""
        for j in range(n):
            if L1[i][j]:
                temp += "#"
            else:
                temp += " "
        answer.append(temp)
    return answer