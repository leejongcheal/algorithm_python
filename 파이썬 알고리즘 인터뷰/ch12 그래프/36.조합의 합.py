from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 전의 풀이는 정렬을 안해도 됨 -> 211111111 같은 값이 들어가기 때문에
        # 근데 이풀이는 for문에서 now_som + L[next]값이 target보다 크다면
        # for문에대해서 break 쳐서 다음을 검사안함 -> 시간적으로 좋음
        # 따라서 정렬을 해서 시간효율을 높인것 - 차이점을 알고 써야함
        candidates = sorted(candidates)
        res = []
        def dfs(index, now = []):
            now_sum = sum(now)
            if now_sum == target:
                res.append(now)
                return
            for i in range(index, len(candidates)):
                num = candidates[i]
                if now_sum + num <= target:
                    dfs(i, now + [num])
                else:
                    break
        dfs(0)
        return res

print(Solution().combinationSum([2,7,6,3,5,1], 9))