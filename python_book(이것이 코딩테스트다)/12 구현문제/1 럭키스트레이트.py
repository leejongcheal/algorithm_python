n = input()
A = list(map(int, list(n[0:len(n)//2])))
B = list(map(int, list(n[len(n)//2:])))
if sum(A) == sum(B):
    print("l")
else:
    print("R")