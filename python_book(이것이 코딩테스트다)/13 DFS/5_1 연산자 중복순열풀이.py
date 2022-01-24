plus = 0
minus = 1
muti = 2
divide = 3
def deepo_copy(L):
    C = []
    for l in L:
        C.append(l)
    return C



def repeat_permutaion(mod, N):
    ret = []
    if N == 1:
        for i in range(4):
            if mod[i] != 0:
                ret.append([i])
    else:
        for i in range(4):
            if mod[i] != 0:
                C = deepo_copy(mod)
                C[i] -= 1
                for temp in repeat_permutaion(C, N-1):
                    ret.append([i] + temp)
    return ret


N = int(input())
A = list(map(int, input().split()))
mod = list(map(int,input().split()))
Min = int(1e9)
Max = int(-1*(1e9))
for mod_list in repeat_permutaion(mod, sum(mod)):
    ret = A[0]
    for i in range(1, N):
        if mod_list[i-1] == plus:
            ret += A[i]
        if mod_list[i-1] == minus:
            ret -= A[i]
        if mod_list[i-1] == muti:
            ret *= A[i]
        if mod_list[i-1] == divide:
            if ret * A[i] < 0:
                ret = -1 * ( abs(ret) // abs(A[i]))
            else:
                ret //= A[i]
    Min = min(ret, Min)
    Max = max(ret, Max)
print(Max)
print(Min)
