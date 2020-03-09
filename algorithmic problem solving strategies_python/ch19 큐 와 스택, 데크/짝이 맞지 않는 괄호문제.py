from collections import deque
import sys
dic = {')': '(', '}': '{', ']': '[', '>': '<'}
read = sys.stdin.readline
ans = []
T = int(read())
for _ in range(T):
    flag = 1
    q = deque()
    L = read().strip()
    for c in L:
        if c == '(' or c == '{' or c == '[' or c == '<':
            q.append(c)
        elif c == ')' or c == '}' or c == ']' or c == '>':
            if len(q) == 0:
                flag = 0
                break
            elif dic[c] != q.pop():
                flag = 0
                break
        else:
            continue
    if len(q) == 0 and flag == 1:
        ans.append("YES")
    else:
        ans.append("NO")
for a in ans:
    sys.stdout.write("{}\n".format(a))
