N,score,P = map(int,input().split())
if N == 0:
    print(1)
else:
    L = list(map(int, input().split()))
    S = [[x,1] for x in L]
    S.append([score,0])
    S.sort(reverse=True)
    idx = S.index([score,0])
    if idx + 1 > P:
        print(-1)
        exit()
    for i in range(len(S)):
        if S[i][0] == score:
            print(i+1)
            exit()
