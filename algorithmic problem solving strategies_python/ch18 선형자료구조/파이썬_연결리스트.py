class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.next = n2
n2.next = n3
node = n1
while node:
    print(node.data)
    node = node.next

