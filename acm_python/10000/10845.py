import sys
t = int(input())
q = []
res = []
L = sys.stdin.read().splitlines()
for idx in range(t):
    a,*b = L[idx].split()
    if "push" in a:
        q.append(b[0])
    elif a == "front":
        res.append(q[0] if q else "-1")
    elif a == "back":
        res.append(q[-1] if q else "-1")
    elif a == "size":
        res.append(str(len(q)))
    elif a == "empty":
        res.append('0' if q else "1")
    elif a == "pop":
        res.append(q.pop(0) if q else "-1")
print("\n".join(res))
