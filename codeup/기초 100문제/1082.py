import sys

a = sys.stdin.readline().rstrip()
b = int(a, 16)
for i in range(1, 16):
    print("%s*%s=%s" % (a, format(i, "X"), format(i * b, "X")))
