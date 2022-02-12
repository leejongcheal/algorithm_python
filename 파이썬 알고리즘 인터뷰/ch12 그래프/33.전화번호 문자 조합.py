from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, now):
            if index == len(digits):
                res.append(now)
                return
            list = dic[digits[index]]
            for s in list:
                dfs(index + 1, now + s)

        if digits == "":
            return []
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        dfs(0,"")
        return res


print(Solution().letterCombinations(""))