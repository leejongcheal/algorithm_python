class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(strs):
            return strs == strs[::-1]
        res = s[0]
        for start in range(len(s)):
            end = start + len(res)
            while end < len(s):
                if check(s[start:end+1]):
                    if len(res) < end - start + 1:
                        res = s[start:end+1]
                end += 1
        return res




strs = "babad"
print(Solution().longestPalindrome(strs))
