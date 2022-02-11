class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # 와 요런식으로 깔끔하게 ㅋㅋ
        table = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        for char in s:
            if char not in table:
                stack.append(char)
            # 나는 not stack 을 따로 두었는데 이런식으로 깔끔하게
            elif not stack or table[char] != stack.pop():
                return 0
            # 비어 있으면 1 리턴 아니면 0리턴을 이런식으로
        return len(stack) == 0


print(Solution().isValid(")("))