def check(u):
    q = []
    for i in range(len(u)):
        if u[i] == "(":
            q.append("(")
        elif u[i] == ")":
            if q:
                q.pop()
            else:
                return 0
    if q:
        return 0
    else:
        return 1


def split(p):
    N = len(p)
    u, v = "",""
    left = 0
    right = 0
    for i in range(N):
        if p[i] == "(":
            left += 1
        elif p[i] == ")":
            right += 1
        if left == right and left != 0:
            u = p[0:i + 1]
            v = p[i+1:]
            return u, v

def solution(p):
    if check(p) == 1:
        return p
    if len(p) == 0:
        return ""
    u, v = split(p)
    if check(u):
        return u + solution(v)
    else:
        temp = "("
        temp += solution(v) + ")"
        for i in range(1,len(u)-1):
            if u[i] == "(":
                temp += ")"
            else:
                temp += "("
        return temp


p = input()
print(solution(p))
