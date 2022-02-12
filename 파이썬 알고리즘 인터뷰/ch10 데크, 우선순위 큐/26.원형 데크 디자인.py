from collections import deque
class MyCircularDeque:

    def __init__(self, k: int):
        self.max_size = k
        self.size = 0
        self.q = deque()
    def insertFront(self, value: int) -> bool:
        if self.size == self.max_size:
            return 0
        self.q.insert(0, value)
        self.size += 1
        return 1
    def insertLast(self, value: int) -> bool:
        if self.size == self.max_size:
            return 0
        self.q.append(value)
        self.size += 1
        return 1
    def deleteFront(self) -> bool:
        if self.size == 0:
            return 0
        else:
            self.q.popleft()
            self.size -= 1
            return 1
    def deleteLast(self) -> bool:
        if self.size == 0:
            return 0
        else:
            self.q.pop()
            self.size -= 1
            return 1
    def getFront(self) -> int:
        if self.size == 0:
            return -1
        else:
            return self.q[0]
    def getRear(self) -> int:
        if self.size == 0:
            return -1
        else:
            return self.q[-1]
    def isEmpty(self) -> bool:
        return self.size == 0
    def isFull(self) -> bool:
        return self.size == self.max_size

myCircularDeque = MyCircularDeque(3);
print(myCircularDeque.insertLast(1));  #// return True
print(myCircularDeque.insertLast(2));  #// return True
print(myCircularDeque.insertFront(3)); #// return True
print(myCircularDeque.insertFront(4)); #// return False, the queue is full.
print(myCircularDeque.getRear());      #// return 2
print(myCircularDeque.isFull());       #// return True
print(myCircularDeque.deleteLast());   #// return True
print(myCircularDeque.insertFront(4)); #// return True
print(myCircularDeque.getFront());     #// return 4
