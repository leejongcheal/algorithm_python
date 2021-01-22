n = input()
alpa = []
num = []
for c in n:
    if 'A' <= c <= 'Z':
        alpa.append(c)
    else:
        num.append(int(c))
alpa.sort()
print(''.join(alpa) + str(sum(num)))