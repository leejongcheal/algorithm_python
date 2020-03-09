def quick_sort(L):
    def sort(low, high):
        if high <= low:
            return
        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = L[(low + high) // 2]
        while low <= high:
            while L[low] < pivot:
                low += 1
            while L[high] > pivot:
                high -= 1
            if low <= high: # 같은경우에도 값을 변경해서 탈출하기 위함
                L[low], L[high] = L[high], L[low]
                low += 1
                high -= 1
        return low

    sort(0, len(L) - 1)


L = [int(a) for a in input().split()]
quick_sort(L)
print(L)
