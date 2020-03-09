def check_pwd(s):
    flag = 0
    n = len(s)
    for i in range(1, n//2):
        for j in range(0, n-i*2+1):
            if s[j:j+i] == s[j+i:j+2*i]:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 1:
        print("Rejected")
    else:
        print("Accepted")


T = int(input())
for _ in range(T):
    s = input()
    check_pwd(s)
