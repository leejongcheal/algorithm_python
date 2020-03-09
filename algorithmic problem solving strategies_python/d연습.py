class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


a = Node(12)
node = a.right
node = Node(2)
print(a.right)
