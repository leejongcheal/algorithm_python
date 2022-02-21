from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        cnt = Counter()
        for right in range(len(s)):
            cnt[s[right]] += 1
            max_char_n = cnt.most_common(1)[0][1]
            # 만족하지 못한경우 시작점만 +1 해줌
            # 왜냐면 만족한경우에는 start를 그대로 둬서 지금 크기보다 큰 슬라이등에
            # 대해서만 검사를 하는식으로 하면되니깐 -> 복습때 조건만족하지 않을때
            # 투포인터 이동을 자세히 정의하지못함
            if right + 1 - left - max_char_n > k:
                cnt[s[left]] -= 1
                left += 1
        return right + 1 - left

s = "AAABBC"
print(Solution().characterReplacement("A",0))

