from collections import defaultdict
class Solution:
    # 재귀구조 브루트 포스
    # def fib(self, n: int) -> int:
    #     if n <= 1:
    #         return n
    #     return self.fib(n-1) + self.fib(n-2)

    # 상향식 - 타뷸레이션
    # def fib(self, n: int) -> int:
    #     res = [0]*(n+3)
    #     res[0],res[1] = 0, 1
    #     for i in range(2,n+1):
    #         res[i] = res[i-1] + res[i-2]
    #     return res[n]
    
    # 하향식 - 메모리제이션
    # DP = defaultdict(int)
    # def fib(self, n: int) -> int:
    #     if n <= 1:
    #         return n
    #     if not self.DP[n]:
    #         self.DP[n] = self.fib(n-1) + self.fib(n - 2)
    #     return self.DP[n]

    # 상향식 비슷한데 공간 절약
    def fib(self, n: int) -> int:
        x, y = 0, 1
        for i in range(n):
            x, y = y, x + y
        return x



print(Solution().fib(6))