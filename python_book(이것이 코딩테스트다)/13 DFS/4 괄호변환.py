# 올바른지 검사 --> 인수는 균형잡힌값만 들어가야함
def check_balance(string):
    cnt = 0
    n = len(string)
    for i in range(n):
        if string[i] == "(":
            cnt += 1
        elif string[i] == ")":
            if cnt == 0:
                return -1
            cnt -= 1
    return 1

def cut_string(string):
    n = len(string)
    cnt = 0
    index = 1e9
    for i in range(n):
        if string[i] == "(":
            cnt += 1
            if cnt == 0:
                index = i
                break
        elif string[i] == ")":
            cnt -= 1
            if cnt == 0:
                index = i
                break
    if index == 0:
        return "", string
    elif index == 1e9 or index == n-1:
        return string, ""
    else:
        return string[0:index+1], string[index+1:]
## 훨씬 간단한 방법
# def seperate(p):
#     u, v = "", ""
#     left_cnt = 0
#     for i in range(len(p)):
#         if p[i] == "(":
#             left_cnt += 1
#         else:
#             left_cnt -= 1
#         if left_cnt == 0:
#             u += p[0:i+1]
#             v += p[i+1:]
#             break
#     return u, v

def solution(p):
    if len(p) == 0:
        return p
    u, v = cut_string(p)
    print(u+"  "+v)
    if check_balance(u) == 1 and len(u) != 0:
        return u + solution(v)
    else:
        if len(u) == 0:
            return "(" + solution(v) + ")"
        else:
            s = ""
            for i in range(1,len(u)-1):
                if u[i] == "(":
                    s += ")"
                else:
                    s += "("
            return "(" + solution(v) + ")" + s

p = input()
print(solution(p))


