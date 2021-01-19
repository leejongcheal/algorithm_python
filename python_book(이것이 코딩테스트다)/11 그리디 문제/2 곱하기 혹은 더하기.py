L = list(map(int,list(input())))
result = 0
for i in L:
    if i == 0 or i == 1 or result == 0 or result == 1:
        result += i
    else:
        result *= i
print(result)