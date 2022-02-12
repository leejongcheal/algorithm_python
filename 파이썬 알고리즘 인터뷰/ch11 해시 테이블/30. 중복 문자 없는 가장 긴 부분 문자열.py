class Solution:
    def lengthOfLongestSubstring(self, S: str) -> int:
        max_size = 0
        start, end = 0, 0
        for end in range(len(S)):
            s = S[end]
            if s in S[start:end]:
                for start in range(start, end):
                    if S[start] == S[end]:
                        start += 1
                        break
            max_size = max(max_size, end - start + 1)
        return max_size


print(Solution().lengthOfLongestSubstring("abcabcaa"))