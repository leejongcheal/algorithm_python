import sys
sys.setrecursionlimit(10**8)
tt = dict()  # 한점의 경로의 최댓값 넣어줘서 재활용하기위함


# r,c:위치 v:여태 지나온 알파벳경로 순서대로 있는 문자열
def DFS(r,c, v):
    global n,R,C
    global tt
    k = r,c,v
    if k in tt.keys():
        return tt[k]
    elif r < 0 or r >= R or c < 0 or c >= C:
        return 0
    elif n[r][c] in v:
        return 0
    vv = v + n[r][c]
    tt[k] = max(DFS(r+1,c,vv),DFS(r-1,c,vv),DFS(r,c+1,vv),DFS(r,c-1,vv)) + 1
    return tt[k]
    # 상하좌우 확인


R, C = map(int, input().split())
a = sys.stdin.read().splitlines()
n = []
result = 0
for i in range(R):
    n.append((a[i]))
print(DFS(0,0,""))
