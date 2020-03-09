def find_next_index(i,s):
    global L
    try:
        return L.index(s,i)
    except:
        return 101


def find_min(i,C):
    max_idx = 0
    max = find_next_index(i,C[0])
    for x in range(1,len(C)):
        a = find_next_index(i,C[x])
        if max < a:
            max = a
            max_idx = x
    return max_idx


N,K = map(int,input().split())
L = list(map(int,input().split()))
C = []
c = 0
result = 0
for i in range(K):
    if c != N:
        if L[i] in C:
            continue
        else:
            c += 1
            C.append(L[i])
    else:
        if L[i] in C:
            continue
        else:
            min = find_min(i,C)
            result += 1
            C[min] = L[i]
print(result)
