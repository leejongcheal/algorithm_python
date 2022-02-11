# 굳이 deque 에 popleft를 사용해서 풀생각 안함  귀찮아
# 구조체 선언과 사용방법만 눈여겨 보기
class MyStack:

    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        return self.q.pop()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0


myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top())  # return 2
print(myStack.pop())  # return 2
print(myStack.pop())  # return 1
print(myStack.empty())  # return True
