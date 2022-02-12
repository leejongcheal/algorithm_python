import collections


# Definition for singly-linked list.
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
class MyHashMap:

    def __init__(self):
        self.table = collections.defaultdict(ListNode)
        self.size = 1000
    def put(self, key: int, value: int) -> None:
        index = key % self.size
        node = ListNode(key, value)
        # 해당 index 아무것도 없는 경우
        if self.table[index].value is None:
            self.table[index] = node
        # 해당 index에 여러가지 있어서 뒤쪽에 넣어줘야하는경우
        else:
            now = self.table[index]
            while now is not None:
                if now.key == key:
                    now.value = value
                    return
                if now.next is None:
                    break
                now = now.next
            now.next = node
        return None
    def get(self, key: int) -> int:
        index = key % self.size
        now = self.table[index]
        # now.value가 0인경우도 있으니 value에 대해서 is not None으로 해야함
        while now and now.value is not None:
            if now.key == key:
                return now.value
            now = now.next
        return -1
    def remove(self, key: int) -> None:
        index = key % self.size
        # 아무것도 없는경우
        if self.table[index].value is None:
            return None
        # 인덱스의 첫 번째 노드일때 삭제 처리
        now = self.table[index]
        if now.key == key:
            if now.next is None:
                self.table[index] = ListNode()
            else:
                self.table[index] = now.next
            return
        # 연결 리스트 노드 삭제
        prev = now
        now = now.next
        while now:
            if now.key == key:
                prev.next = now.next
                return
            prev, now = now, now.next

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
