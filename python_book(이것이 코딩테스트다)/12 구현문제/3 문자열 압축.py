def solution(s):
    res = len(s)
    if res < 2:
        return res
    for seq in range(1, len(s)//2+1):
        temp_s = ""
        pre = s[0:seq]
        r = len(s) // seq
        cnt = 1
        for i in range(1,r):
            now = s[i*seq:(i+1)*seq]
            if now == pre:
                cnt += 1
            else:
                if cnt != 1:
                    temp_s += pre+str(cnt)
                    cnt = 1
                else:
                    temp_s += pre
                    cnt = 1
            pre = now
        # 끝나고 나서 남은 pre에 대해서도 처리해주기
        if cnt != 1:
            temp_s += pre+str(cnt)
        else:
            temp_s += pre
        # 나머지에 대해서 붙여주기
        temp_s += s[r*seq:len(s)]
        res = min(res,len(temp_s))
    return res
s = input()
print(solution(s))