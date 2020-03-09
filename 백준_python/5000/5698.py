import sys
input = sys.stdin.readline
res = []
while True:
    a = input().split()
    if a == ["*"]:
        print("\n".join(res))
        exit()
    res.append("Y")
    for i in range(len(a)-1):
        if a[i][0].lower() != a[i+1][0].lower():
            res[-1] = "N"
            break