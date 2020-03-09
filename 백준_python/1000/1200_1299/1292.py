def search_row(n):
    for i in range(1,n+1):
        if 2 * n <= i * (i + 1):
            return i

A,B = map(int,input().split())
a = search_row(A)
b = search_row(B)
# print(a,b,1212)
sum_a = a - (A - (((a-1)*a)//2 + 1))
sub_b = B - ((b-1)*b//2)
# print(sum_a,sub_b)
sum = 0
for i in range(a,b+1):
    if i == a and i == b:
        sum += i*(B-A+1)
    elif i == a:
        sum += i*sum_a
    elif i == b:
        sum += i*sub_b
    else:
        sum += i*i
print(sum)

