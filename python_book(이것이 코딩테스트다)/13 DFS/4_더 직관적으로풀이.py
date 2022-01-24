def divide(W):
    left = 0
    right = 0
    for i in range(len(W)):
        if W[i] == "(":
            left += 1
        elif W[i] == ")":
            right += 1
        if left == right:
            index = i
            break
    u = W[0:index + 1]
    v = W[index+1:]
    return u, v


def check(u):
    q = []
    for s in u:
        if s == "(":
            q.append(s)
        else:
            if len(q) == 0:
                return 0
            else:
                q.pop()
    if len(q) == 0:
        return 1
    else:
        return 0


def reverse(u):
    if len(u) == 2:
        return ""
    ret = ""
    for s in u[1:-1]:
        if s == "(":
            ret += ")"
        else:
            ret += "("
    return ret


def solution(p):
    if p == "":
        return ""
    u, v = divide(p)
    if check(u):
        return u + solution(v)
    ret = "("
    ret += solution(v)
    ret += ")"
    ret += reverse(u)
    return ret


W = input()
print(solution(W))