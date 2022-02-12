class MyHashMap:

    def __init__(self):
        self.dic = dict()
    def put(self, key: int, value: int) -> None:
        self.dic[key] = self.dic.get(key, [])
        self.dic[key].append(value)
    def get(self, key: int) -> int:
        return self.dic.get(key, [-1])[-1]
    def remove(self, key: int) -> None:
        if self.dic.get(key, 0) != 0:
            del self.dic[key]


myHashMap = MyHashMap();
print(myHashMap.put(1, 1))#; // The map is now [[1,1]]
print(myHashMap.put(2, 2))#; // The map is now [[1,1], [2,2]]
print(myHashMap.get(1))#;    // return 1, The map is now [[1,1], [2,2]]
print(myHashMap.get(2))#;    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
print(myHashMap.put(2, 1))#; // The map is now [[1,1], [2,1]] (i.e., update the existing value)
print(myHashMap.get(2))#;    // return 1, The map is now [[1,1], [2,1]]
print(myHashMap.remove(2))#; // remove the mapping for 2, The map is now [[1,1]]
print(myHashMap.remove(2))#; // remove the mapping for 2, The map is now [[1,1]]
print(myHashMap.get(2))#;    // return -1 (i.e., not found), The map is now [[1,1]]
# myHashMap.put(3,11)
# myHashMap.put(4, 13)
# myHashMap.put(15, 6)
# myHashMap.put(6, 15)
# myHashMap.put(8,8)
# myHashMap.put(11,0)
# print(myHashMap.table[11].value)
# print(myHashMap.get(11))
# myHashMap.put(1,10)
# myHashMap.put(12,14)
