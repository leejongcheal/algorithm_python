# https://programmers.co.kr/learn/courses/30/lessons/17677

from collections import Counter
def plus_AB(A, B):
    res = 0
    a = set(A.keys())
    b = set(B.keys())
    plus_ab = a | b
    for element in plus_ab:
        if element in a and element in b:
            res += max(A[element], B[element])
        elif element in a:
            res += A[element]
        else:
            res += B[element]
    return res

def minus_AB(A, B):
    res = 0
    a = set(A.keys())
    b = set(B.keys())
    minus_ab = a & b
    for element in minus_ab:
        if element in a and element in b:
            res += min(A[element], B[element])
        elif element in a:
            res += A[element]
        else:
            res += B[element]
    return res

def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    temp1 = str1
    str2 = str2.lower()
    temp2 = str2
    # for char in str1:
    #     if "a" <= char <= "z":
    #         temp1 += char
    # for char in str2:
    #     if "a" <= char <= "z":
    #         temp2 += char
    str1, str2 = [], []
    for i in range(len(temp1) - 1):
        if "a" <= temp1[i] <= "z" and "a" <= temp1[i+1] <= "z":
            str1.append(temp1[i] + temp1[i+1])
    for i in range(len(temp2) - 1):
        if "a" <= temp2[i] <= "z" and "a" <= temp2[i + 1] <= "z":
            str2.append(temp2[i] + temp2[i+1])
    str1 = Counter(str1)
    str2 = Counter(str2)
    plus = plus_AB(str1, str2)
    minus = minus_AB(str1, str2)
    if plus == 0 and minus == 0:
        return 65536
    else:
        return int((minus / plus)*65536)