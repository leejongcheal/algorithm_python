def quick_sort(L):
    n = len(L)
    if n < 2:
        return L
    left = []
    right = []
    equal = [] # 정렬에서 비교값이 같은 경우를 예외처리 꼭 생각
    pivot = L[n//2]
    for i in L:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            equal.append(i)
    left = quick_sort(left)
    right = quick_sort(right)
    return left + equal + right


L = [int(a) for a in input().split()]
print(quick_sort(L))


