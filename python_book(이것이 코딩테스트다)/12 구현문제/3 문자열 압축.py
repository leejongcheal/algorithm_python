INF = int(1e9)
def solution(s):
    l = len(s)
    # 0 인경우 무시할려고 INF 넣어줌
    res = [INF]*(l//2 + 10)
    # 3이하인경우 하나씩만 가능해서 자신을 리턴 \
    if l <= 1:
        return l
    # 1부터 l//2 까지 하나하나 계산후 최솟값 반환
    for i in range(1,l//2+1):
        num = i
        index = 0
        set_s = s[index:index+i]
        index += i
        flag = 0
        # 끝 or 끝의 전까지만 계산 나중에 예외처리로 더해줌
        while index + i <= l:
            # 같은경우 몇개 같은지 flag에 계산
            if set_s == s[index:index+i]:
                flag += 1
            # 다른경우 새로운 쌍의 문자열수를 넣어주고 set_s 갱신
            else:
                # 달라진 경우 숫자의 자릿수 만큼 num 에 넣어주기
                if flag != 0:
                    num += len(str(flag + 1))
                flag = 0
                num += i
                set_s = s[index:index+i]
            index += i
        # 마지막에 계속 같게온 경우 flag에 대해서 계산해줘야함
        if flag != 0:
            num += len(str(flag + 1))
        # 딱 떨어지는경우
        if index == l:
            res[i] = num
        # 끝에 남는 경우 하나씩 더해줌
        else:
            res[i] = num + l - index
    return min(res)


s = input()
print(solution(s))