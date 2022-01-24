def solution(Map, N, M):



for test_case in range(int(input())):
    Map = []
    N, M = map(int, input().split())
    result = 0
    for _ in range(N):
        temp = []
        W = input()
        for i in range(M):
            if W[i] == "#":
                temp.append(1)
            else:
                temp.append(0)
        Map.append(temp)
    solution(Map, N, M)
    print(result)