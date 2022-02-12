class Solution:
    def lengthOfLongestSubstring(self, S: str) -> int:
        max_size = 0
        start, end = 0, 0
        for end in range(len(S)):
            s = S[end]
            if s in S[start:end]:
                start = S[start:end].index(s) + start + 1
            max_size = max(max_size, end - start + 1)
        return max_size


print(Solution().lengthOfLongestSubstring("abcabcaa"))