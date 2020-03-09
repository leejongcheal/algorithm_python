# 삽입 정렬
def insert_sort(L):
    n = len(L)
    # 1~ n-1 까지 반복
    for i in range(1,n):
        key = L[i]
        # 0 번까지 해야하니 -1로 설정(-1+1 = 0)
        for j in range(i-1, -1, -1):
            if key < L[j]: # key보다 크다면 앞자리를 가져야하니 스왑
                L[j+1], L[j] = L[j], L[j+1]
            else: # 자리가 정해짐과 break
                L[j+1] = key
                break
        # print(L)


L = [int(a) for a in input().split()]
insert_sort(L)
print(L)

