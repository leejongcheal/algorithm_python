import sys
def make_box(n):
    if n == 1:
        return "#"
    res = ""
    for i in range(n):
        if i == 0:
            res += "#"*n+"\n"
        elif i == n-1:
            res += "#"*n
        else:
            res += "#"+ "J"*(n-2)+"#\n"
    return res


t = int(input())
name = sys.stdin.read().splitlines()
for idx in range(t):
    print(make_box(int(name[idx])), end="")
    if idx != t - 1:
        print("\n")
