N = int(input())
f = int(input())
a = N // 100 * 100
for i in range(100):
    if (a+i) % f == 0:
        print("%02d" % i)
        break
