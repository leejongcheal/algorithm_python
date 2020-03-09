import sys


def merge_sort(L):
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    leftL = L[:mid]
    rightL = L[mid:]
    leftL = merge_sort(leftL)
    rightL = merge_sort(rightL)
    return merge(leftL, rightL)


def merge(left, right):
    result = []
    global r
    ra = 0
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                ra += len(left)
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    r += ra
    return result


t = int(input())
name = sys.stdin.read().splitlines()
res = []
for idx in range(0, 2 * t, 2):
    n = int(name[idx])
    L = list(map(int, name[idx + 1].split()))
    r = 0
    merge_sort(L)
    res.append(r)
print("\n".join(map(str, res)))
