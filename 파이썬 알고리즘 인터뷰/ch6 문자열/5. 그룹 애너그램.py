from collections import defaultdict

anagram = defaultdict(list)
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
for word in strs:
    sword = "".join(sorted(word))
    anagram[sword].append(word)
print(list(anagram.values()))
