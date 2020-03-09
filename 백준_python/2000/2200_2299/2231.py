N = int(input())
for i in range(len(str(N))*9, 0, -1):
    # print(str(N-i))
    if N-i > 0 and i == sum(map(int, str(N-i))):
        print(N-i)
        exit()
print(0)
