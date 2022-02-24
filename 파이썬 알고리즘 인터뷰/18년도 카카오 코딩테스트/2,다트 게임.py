def solution(dartResult):
    answer = 0
    score = []
    number = -1
    flag = 0
    for i, char in enumerate(dartResult):
        if "0" <= char <= "9":
            if flag == 0:
                number = int(char)
                flag = 1
                continue
            elif flag:
                # 10의 경우 처리
                flag = 0
                number *= 10
                number += int(char)
                continue
        elif char == "S" or char == "D" or char == "T":
            flag = 0
            if char == "D":
                number **= 2
            elif char == "T":
                number **= 3
        elif char == "*":
            flag = 0
            if score:
                score[-1] = score[-1]*2
            number *= 2
        elif char == "#":
            flag = 0
            number *= -1
        if i+1 >= len(dartResult) or "0" <= dartResult[i+1] <= "9":
            score.append(number)

    return sum(score)