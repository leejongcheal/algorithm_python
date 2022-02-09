import re
from collections import Counter
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
paragraph = re.sub('[\W]'," ",paragraph.lower())
words = [word for word in re.sub('[\W]]', " ",paragraph.lower()).split() if word not in banned]
counter = Counter(words)
print(counter.most_common(1)[0][0])
"""
아 솔직히 풀수는 있는데 요런식으로 푸는건 너무 역겹긴하네 진짜로 배운다는 마인드로 하긴하는데 
Counter를 써야하는 경우가 한정적인데 시발 ㅋㅋ
Counter.most_common(index, [index2]): 갯수가 index번째 [~ index2]까지 의 원소를 리스트화해서 반환 
"""