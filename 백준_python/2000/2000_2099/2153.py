import math


def is_prime(n):
    if n == 1:
        return 1
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return 0
    return 1


s = input()
n = 0
for i in range(len(s)):
    if "a" <= s[i] <= "z":
        n += (ord(s[i])-96)
    else:
        n += (ord(s[i]) - 64)
if is_prime(n) == 1:
    print("It is a prime word.")
else:
    print('It is not a prime word.')
