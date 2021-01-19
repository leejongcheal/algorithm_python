L = input()
cnt = 0
for i in range(len(L)-1):
    if L[i] != L[i+1]:
        cnt += 1
print((cnt+1) // 2)