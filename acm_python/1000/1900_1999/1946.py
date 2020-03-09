import sys
N = int(input())
nameList = sys.stdin.read().splitlines()
idx = 0
for q in range(N):
    L = []
    min = 0  # 앞서 나온 수중 면접 순위가 젤 낮은것
    result = 0
    for i in range(int(nameList[idx])):
        idx += 1
        L.append(list(map(int,nameList[idx].split())))
    idx += 1
    L.sort()
    for i in range(len(L)):
        if i == 0:  # 1인경우
            result += 1
            min = L[i][1]
        else:  # 나머지 경우
            if min < L[i][1]:  # 탈락
                continue
            else:  # 합격
                min = L[i][1]
                result += 1
    print(result)


