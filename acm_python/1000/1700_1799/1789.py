S = int(input())
for i in range(S+2):
    if S*2 == i*(i+1):
        print(i)
        exit()
    elif S*2 < i*(i+1):
        print(i-1)
        exit()
