import sys

name = sys.stdin.read().splitlines()
res = []
for idx in range(len(name) - 1):
    L = list(map(float, name[idx].split()))
    i = L.index(-1)
    print('Triangle #%d' % (idx + 1))
    if i != 2:
        if L[1 - i] >= L[2]:
            print('Impossible.\n')
        else:
            a = (L[2] ** 2 - L[1 - i] ** 2) ** 0.5
            if i == 0:
                print("a = %.3f\n" % a)
            else:
                print("b = %.3f\n" % a)
    else:
        a = (L[0] ** 2 + L[1] ** 2) ** 0.5
        print("c = %.3f\n" % a)
