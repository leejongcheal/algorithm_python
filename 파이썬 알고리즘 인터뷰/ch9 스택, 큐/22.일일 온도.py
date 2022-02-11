from typing import List



"""
ㅋㅋㅋㅋ 스택풀이 했는데 최악의 경우 n^2이긴 한데 타임 오버
시각 통계학 사용했을때, stack에 넣어질떄의 경우 맨위가 젤 작은 온도를 가진다는것을 알았어야 했다.
즉, stack[-1] 에 대해서 현재 온도가 작다면 stack 전체 온도보다 작다는 말이니 검사할필요도 없음
"""
# class Solution:
#     def dailyTemperatures(self, t: List[int]) -> List[int]:
#         res = [0]*len(t)
#         # stack에 남아있는 값들은 0을 가져야하는데 == res연산이 안되어 자동 0값이 넣어짐
#         stack = [0]
#         for i in range(1, len(t)):
#             if t[i] > t[i-1]:
#                 new_stack = []
#                 while stack:
#                     pre = stack.pop()
#                     if t[pre] < t[i]:
#                         res[pre] = i - pre
#                     # 아직 답을 못구한 경우
#                     else:
#                         new_stack.append(pre)
#                 # 원래라면 [::-1] 값을 stack에 넣어주는데 답에는 영향 없으니 걍넣음
#                 stack = new_stack
#             stack.append(i)
#         return res

# 와 진짜 대단하다 걍.
# 전의 값이랑 비교해서 올라가는 경우 stack 검사하는걸로 풀었는데 답지는 그냥 스택보다 크면으로 풀어버렸네
# 위랑 비슷한 개념인데 코딩의 우아함을 볼것 -> 이런생각을 어떻게 해야하냐 진짜 대단하다 걍
class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stack = []
        res = [0]*len(t)
        for i in range(len(t)):
            while stack and t[stack[-1]] < t[i]:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)
        return res

print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))