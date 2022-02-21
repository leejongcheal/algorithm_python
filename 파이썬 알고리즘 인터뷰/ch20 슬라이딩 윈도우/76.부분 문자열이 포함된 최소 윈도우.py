from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(now):
            ## 처음에는 key가 t의 값이고 1이면 ok로함
            ## 근데 t = "aa" 인경우에는 a의 갯수가 2개이상이여야함
            for key in need.keys():
                if now[key] < need[key]:
                    return 0
            return 1
        res = ""
        start = 0
        need = Counter(t)
        now = Counter()
        for index, char in enumerate(s):
            now[char] += 1
            if check(now):
                # 계속 비교를 함으로써 a가 2개필요한데 a가 5개 있는경우든 상관없이 최소만족index + 1값이 start에 들어감
                while check(now):
                    now[s[start]] -= 1
                    start += 1
                if not res or len(res) > index - start + 2:
                    res = s[start-1:index+1]
        return res


# "aa", "a" -> ""// "a", "a" -> "a" 예외처리 ㅋㅋ

s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow("a","aa"))