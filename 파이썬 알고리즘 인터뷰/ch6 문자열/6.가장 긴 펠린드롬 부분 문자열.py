class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            # if right >= len(s):
            #     return ""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # "ac" 인경우에 0,2가 들어오면 s[1:2]로 c 반환됨
            return s[left+1:right]
        # res = s[0]
        res = ""
        # "z" 인경우 z반환하기 위한 예외처리 + s자체가 펠린인경우 시간절약
        if len(s) < 2 or s == s[::-1]:
            return s
        for i in range(len(s)):
            res = max(expand(i,i+1), expand(i,i+2), res,key=len)
        return res




strs = "acd"
print(Solution().longestPalindrome(strs))
