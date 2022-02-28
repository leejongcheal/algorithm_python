from typing import List
import re
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        return Counter([word for word in re.sub("[^a-z]"," ",paragraph.lower()).split()
                 if word not in banned]).most_common(1)[0][0]



paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(Solution().mostCommonWord(paragraph, banned))