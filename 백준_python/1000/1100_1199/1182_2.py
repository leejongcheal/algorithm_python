result = 0
N,S = map(int,input().split())
L = list(map(int,input().split()))
R = []
result = 0
def subset(A,index,L):
    global result
    R = []
    if index == 0:
        for i in L:
            if i == S:
                result += 1
            R.append([i])
    else:
        for a in A:
            for i in L:
                d = a[:]
                if i not in d:
                    d.append(i)
                    # print("d", d, i)
                    d.sort()
                    if d not in R:
                        if sum(d) == S:
                            result += 1
                        R.append(d)
    return R[:]

for r in range(N):
    R = subset(R,r,L)
print(result)

