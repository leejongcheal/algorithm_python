# def binary_search(L, target, start, end):
#     if start > end:
#         return -1
#     mid = (start + end) // 2
#     if L[mid] == target:
#         return mid
#     elif L[mid] < target:
#         start = mid + 1
#     elif L[mid] > target:
#         end = mid - 1
#     return binary_search(L, target, start, end)


n = int(input())
L = [0]*1000000
for i in input().split():
    L[int(i)] = 1
m = int(input())
M = list(map(int, input().split()))
result = []
for i in M:
    # if binary_search(N,i,0,n-1) != -1:
    if L[i] == 1:
        result.append("yes")
    else:
        result.append("no")
print(" ".join(result))







