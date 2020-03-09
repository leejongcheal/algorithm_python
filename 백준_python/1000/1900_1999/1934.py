import sys
def gcd(a,b):
    while b != 0:
        temp = a
        a = b
        b = temp%b
    return a


def gcm(a):
    return (a[0]*a[1])//gcd(a[0],a[1])


N = int(input())
a = list(sys.stdin.read().splitlines())
for i in range(N):
    print(gcm(list(map(int,a[i].split()))))


