def binary_left(L, target, start = 0, end = None):
    if end == None:
        end = len(L)
    while start < end:
        mid = (start + end) // 2
        if L[mid] <= target:
            end = mid
        elif L[mid] > target:
            start = mid + 1
    return start


def binary_right(L, target, start = 0, end = None):
    if end == None:
        end = len(L)
    while start < end:
        mid = (start + end) // 2
        if L[mid] <= target:
            start = mid + 1
        elif L[mid] > target:
            end = mid
    return start

L = [1,2,2,2,3,4]
print(binary_left(L,2))
print(binary_right(L,2))