import sys
a = list(sys.stdin.readline())
for i in range(5):
    print("["+a[i]+"0"*(4-i)+"]")