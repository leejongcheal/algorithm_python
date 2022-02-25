# https://programmers.co.kr/learn/courses/30/lessons/17677
from collections import Counter
def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    L1, L2 = [], []
    for i in range(len(str1) - 1):
        a = str1[i:i+2]
        if a.isalpha():
            L1.append(a)
    for i in range(len(str2) - 1):
        a = str2[i:i+2]
        if a.isalpha():
            L2.append(a)
    str1 = Counter(L1)
    str2 = Counter(L2)
    union = sum((str1|str2).values())
    intersection = sum((str1&str2).values())
    answer = intersection / union if union != 0 else 1
    return int(answer * 65536)


s1 = 'FRANCE'
s2 = 'french'
print(solution(s1,s2))