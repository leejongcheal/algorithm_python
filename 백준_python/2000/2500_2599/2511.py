A = list(input().split())
B = list(input().split())
a = 0
b = 0
last_a = -1
last_b = -1
for i in range(10):
    if A[i] > B[i]:
        a += 3
        if i > last_a:
            last_a = i
    elif A[i] < B[i]:
        b += 3
        if i > last_b:
            last_b = i
    else:
        a += 1
        b += 1
print(a,b)
if a > b:
    print("A")
elif a<b:
    print("B")
else:
    if last_a == -1 and last_b == -1:
        print("D")
    elif last_a > last_b:
        print("A")
    else:
        print("B")
