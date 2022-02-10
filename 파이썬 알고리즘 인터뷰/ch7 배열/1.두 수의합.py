L = list(map(int,input().split()))
target = int(input())
# index를 이용한 풀이 -> 리스트에 find메서드는 없다
# for i, now in enumerate(L):
#     complement = target - now
#     if complement in L[i+1:]:
#         print(i, L.index(complement))
nums_map = {}
for i, now in enumerate(L):
    complemt = target - now
    if complemt in nums_map:
        print(nums_map[complemt], i)
    nums_map[now] = i