from copy import deepcopy
from itertools import permutations, combinations
### 재귀끝내는 기준이 뽑는 N이 1인경우를 무조건 암기해야 순열조합 응용까진 풀이 가능
def perm(L, n):
    N = len(L)
    ret = []
    if N < n:
        return None
    if n == 1:
        for l in L:
            ret.append([l])
    else:
        for i in range(N):
            # L[N] 은 오류남 but L[N:] 은 빈 리스트 반환
            for temp in perm(L[0:i] + L[i+1:], n - 1):
                ret.append([L[i]] + temp)
    return ret


def comb(L, n):
    ret = []
    N = len(L)
    if N < n:
        return None
    if n == 1:
        for i in L:
            ret.append([i])
            # 리스트로 집어 넣어줘야함
    else:
        for i in range(N - n + 1):
            for temp in comb(L[i+1:], n-1):
                ret.append([L[i]] + temp)
                # *** [i] 가 아닌 [L[i]]로 집어넣줘야함
    return ret

# mod = [1, 2, 3, 2] 인 경우 01122244 순의 리스트 뽑기
def repeat_permutaion(mod, N):
    ret = []
    if N == 1:
        for i in range(4):
            if mod[i] != 0:
                ret.append([i])
    else:
        for i in range(4):
            if mod[i] != 0:
                C = deepcopy(mod)
                C[i] -= 1
                for temp in repeat_permutaion(C, N-1):
                    ret.append([i] + temp)
    return ret
L = [1,2,3]
print(list(permutations(L)))
print(perm(L,3))
print(list(permutations(L, 2)))
print(perm(L,2))
print(list(combinations(L,3)))
print(comb(L,3))
print(list(combinations(L,2)))
print(comb(L,2))
''' 내장함수를 이용해서 순열과 조합을 구할때 주의할점
    p = combinations(L,2) 에서 p는 조합의 특정 주소값을 가짐 
    따라서 list(p)로 써야함
    그리고 p의 원소들은 다 튜플타입을 가짐 -> 헷갈린다면 그냥 list화 해서 사용하는게 좋음, 특히 str관련해서 사용하는경우에는
    괴상한 튜플이 나오기 때문에 무조건 list화 해서 str형식으로 변환하는식으로 사용할것 + join관련해서도 리스트가 편하니깐
    list(p)등 을 사용하면 이유는 모르겠는데 p의 주소값이 바껴서 그이후론 p에 대해서 사용할수가 없으므로 
    p = list(p)등으로 타입변환 하는경우 타입변환한 값을 저장해야한다.
'''