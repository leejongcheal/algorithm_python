N = int(input())
L = []
for i in range(N):
    L.append(int(input()))
L = L[::-1]
stack = []
result = []
idx = 1
while L:
    a = L.pop()
    while True:
        if len(stack) == 0:
            stack.append(idx)
            result.append('+')
            idx += 1
        if stack[-1] == a:
            stack.pop()
            result.append('-')
            break
        elif idx > N:
            print("NO")
            exit()
        else:
            stack.append(idx)
            result.append('+')
            idx += 1
for i in result:
    print(i)
