ans = ""
for idx in range(int(input())):
    x,y = input().split()
    x = int(x)
    ans += y[:x-1]+y[x:]+"\n"
print(ans)
