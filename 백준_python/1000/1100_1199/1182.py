result = 0
N,S = map(int,input().split())
L = list(map(int,input().split()))


def printAllSubset(A):
    printAllSubsetHelper(A, 0)


def printAllSubsetHelper(A, index):
    global result
    if index == len(A):
        if len(A) != 0 and sum(A) == S:
            result += 1
        return
    printAllSubsetHelper(A[:], index + 1)  # index번째 원소를 건드리 않고 다음으로 넘어가는 경우
    A.pop(index)  # index번째의 원소를 제외하고
    printAllSubsetHelper(A[:], index)  # 다음 원소로 넘어가는 경우. 주의할 점은 앞서 뺀 원소가 아예 사라졌기 때문에 index를 증가시키면 안된다!


printAllSubset(L)
print(result)

