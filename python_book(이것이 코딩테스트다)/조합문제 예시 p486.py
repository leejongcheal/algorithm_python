"""조합  문제 예시
L개의 비번갯수와 C개의 알파벳 입력받음
최소 모음 1개이상자음 2개이상으로 정렬순으로 L개의 암호를 가진것을 알파벳순으로 출력
combinations의 기본
 - 반환값 : 특정 주소를 가지는 조합타입 [(),(),()..]식으로 반환
 - 원소값 : 튜플형식을 가짐
반환값에 대해서 리스트형으로 형변환과 원소값도 리스트로 형변환 하는게 편하다.
문자열에대한 조합 사용 예시
2개로 나누어서 풀었는데 그냥 다 뽑은 다음에 모음과 자음 갯수를 검사해서 출력하는식으로 푸는게 훨씬 편했을듯
"""
import sys, itertools
input = sys.stdin.readline


L, C = map(int, input().rstrip().split())
result = []
alpa = list(input().rstrip().split())
mo = []
ja = []
for i in alpa:
    if i in "aeoui":
        mo.append(i)
    else:
        ja.append(i)
mo.sort()
for i in range(1, len(mo) + 1):
    if L - i < 2:
        break
    mo_result = list(itertools.combinations(mo, i))
    ja_result = list(itertools.combinations(ja, L - i))
    for mo_data in mo_result:
        for ja_data in ja_result:
            temp = ""
            temp = list(mo_data) + list(ja_data)
            result.append(sorted(temp))
result.sort()
for r in result:
    print("".join(r))
