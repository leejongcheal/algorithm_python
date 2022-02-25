# https://programmers.co.kr/learn/courses/30/lessons/17682
def solution(dartResult):
    answer = 0
    score = [0]
    for char in dartResult:
        if char == "S":
            score[-1] **= 1
            score.append(0)
        elif char == "D":
            score[-1] **= 2
            score.append(0)
        elif char == "T":
            score[-1] **= 3
            score.append(0)
        elif char == "#":
            score[-2] *= -1
        elif char == "*":
            score[-2] *= 2
            if len(score) >= 3:
                score[-3] *= 2
        # 숫자인 경우
        else:
            score[-1] = score[-1]*10 + int(char)
    return sum(score)

s = "1S2D*3T"
print(solution(s))
