from collections import defaultdict as dd

def main():
    m = 26  # number of upper alphabets
    r, c = map(int, input().split())
    board = [list(map(lambda s: 1 << (ord(s)-65), input())) for i in range(r)]  # save char is int 0 ~ 25
    print(board)
    x = dd(lambda: set())  # x[k] represents (k//c, k%c)

    x[0] = {board[0][0]}  # mark as visited]
    z = {}
    def adj(k):
        i, j = k//c, k%c
        if i:
            yield k-c
        if j:
            yield k-1
        if c-j-1:
            yield k+1
        if r-i-1:
            yield k+c

    que = {0}
    for k in range(1, m):
        new_que = set()
        y = dd(lambda: set())
        if not que:
            break
        while que:
            p = que.pop()
            for q in adj(p):
                bean = board[q//c][q%c]
                flag = True
                for b in x[p]:
                    if not bean & b:
                        y[q].add(b | bean)
                        if flag:
                            new_que.add(q)
                            flag = False
        que = new_que
        x = y
        for key in x.keys():
            z[key] = k
    if z:
        #print(z)
        return max(z.values())+1
    return 1

print(main())