from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter, digits = [], []
        for log in logs:
            if log.split()[1].isalpha():
                letter.append(log)
            else:
                digits.append(log)
        letter.sort(key=lambda x: (x.split()[1:] , x.split()[0]))
        return letter + digits

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(Solution().reorderLogFiles(logs))