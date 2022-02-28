class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            if right >= len(s):
                return ""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        res = s[0]
        for i in range(len(s)):
            res = max(expand(i,i+1), expand(i,i+2), res,key=len)
        return res




strs = "acd"
print(Solution().longestPalindrome(strs))
