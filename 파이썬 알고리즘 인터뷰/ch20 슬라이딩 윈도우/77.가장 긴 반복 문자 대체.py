from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        mapper = defaultdict(int)
        max_repeat = 0
        # max_length = 0
        for right, letter in enumerate(s):
            # counter를 안쓰는 경우 속도가 훨씬 빠름 -> 근데 왜? -> most_commos가 문제
            mapper[letter] += 1
            max_repeat = max(max_repeat, mapper[letter])
            if right - left + 1 - max_repeat > k:
                mapper[s[left]] -= 1
                left += 1
        # return max_length
        # 제일 큰 size를 유지하면서 조사를 했으니 이게 답이됨
        return right - left + 1

s = "AAABBC"
# print(Solution().characterReplacement("A",0))
print(Solution().characterReplacement(s,2))