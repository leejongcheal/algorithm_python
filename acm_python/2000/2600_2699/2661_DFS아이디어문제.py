def check(res):
    n = len(res)
    for i in range(1,n//2+1):
        if res[n-i:n] == res[n-2*i:n-i]:
            return - 1
    return 1


def DFS(res):
    if check(res) == -1:
        return
    if len(res) == n:
        print(res)
        exit()
    for i in "123":
        DFS(res+i)
    return


n = int(input())
ans = ""
DFS(ans)
