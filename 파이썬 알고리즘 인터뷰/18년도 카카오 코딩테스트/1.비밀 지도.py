# https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3
def solution(n, arr1, arr2):
    maps = []
    for i in range(n):
        maps.append(
        bin(arr1[i]|arr2[i])[2:].zfill(n).replace("1","#").replace("0"," ")
        )
    return maps

arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(5,arr1,arr2))


# str.zfill(10) 문자열에 대해서 str의 길이가 10보다 작으면 왼쪽에 남은수만큼 0으로 채워준다.
# bin(32) = 0b100000
# 32|31 = 63 숫자에 대해서 비트연산가능
