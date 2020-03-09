# 입력 int 숫자를 받아서 오름차순 선택 정렬
def sel_sort(L):
    n = len(L)
    print(n)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if L[min_idx] > L[j]:
                min_idx = j
        L[i], L[min_idx] = L[min_idx], L[i]


L = [int(a) for a in input().split()]
# sorted(L)
sel_sort(L)
print(L)
