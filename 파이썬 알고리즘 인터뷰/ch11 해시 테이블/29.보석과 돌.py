class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freq = dict()
        count = 0
        for char in S:
            freq[char] = freq.get(char, 0) + 1
        for char in J:
            count += freq.get(char, 0)
        return count


print(Solution().numJewelsInStones("aA", "aAAbbbb"))