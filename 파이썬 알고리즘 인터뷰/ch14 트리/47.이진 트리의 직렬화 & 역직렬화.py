from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Codec:
    # 직렬화
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        result = ["#"]
        q = deque([root])
        while q:
            now = q.popleft()
            if now:
                result.append(str(now.val))
                q.append(now.left)
                q.append(now.right)
            else:
                result.append("#")
        return " ".join(result)

    # 역직렬화
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        data = list(data.split())
        if data[1] == "#":
            return None
        root = TreeNode(int(data[1]))
        q = deque([root])
        now_index = 1
        while q:
            now = q.popleft()
            if now_index + 2 < len(data):
                l, r = data[now_index + 1], data[now_index + 2]
                if l != "#":
                    now.left = TreeNode(int(data[now_index + 1]))
                    q.append(now.left)
                else:
                    now.left = None
                if r != "#":
                    now.right = TreeNode(int(data[now_index + 2]))
                    q.append(now.right)
                else:
                    now.right = None

                now_index += 2
        return root
# root = None
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
root.right.left.left = TreeNode(6)
root.right.left.right = TreeNode(7)

a = Codec().serialize(root)
print(a)
b = Codec().deserialize(a)
print(1)

