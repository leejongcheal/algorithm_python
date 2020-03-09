def binary_search(item):
    global A
    low = 0
    high = len(A)-1
    while low <= high:
        mid = (low + high)//2
        if item == A[mid]:
            return 1
        elif item > A[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return 0


N = int(input())
A = list(map(int,input().split()))
A.sort()
M = int(input())
B = list(map(int,input().split()))
for i in B:
    print(binary_search(i))


