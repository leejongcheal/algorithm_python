from collections import deque
class MyCircularQueue:

    def __init__(self, k: int):
        self.q = deque()
        self.max_size = k
        self.now_size = 0
    def enQueue(self, value: int) -> bool:
        if self.max_size == self.now_size:
            return 0
        self.q.append(value)
        self.now_size += 1
        return 1
    def deQueue(self) -> bool:
        if self.now_size == 0:
            return 0
        self.now_size -= 1
        self.q.popleft()
        return 1
    def Front(self) -> int:
        if self.now_size == 0:
            return -1
        return self.q[0]
    def Rear(self) -> int:
        if self.now_size == 0:
            return -1
        return self.q[-1]
    def isEmpty(self) -> bool:
        if self.now_size == 0:
            return 1
        else:
            return 0

    def isFull(self) -> bool:
        if self.now_size == self.max_size:
            return 1
        else:
            return 0


myStack = MyCircularQueue(3)
print(myStack.enQueue(1)); #// return True
print(myStack.enQueue(2)); #// return True
print(myStack.enQueue(3)); #// return True
print(myStack.enQueue(4)); #// return False
print(myStack.Rear());     #// return 3
print(myStack.isFull());   #// return True
print(myStack.deQueue());  #// return True
print(myStack.enQueue(4)); #// return True
print(myStack.Rear());     #// return 4
