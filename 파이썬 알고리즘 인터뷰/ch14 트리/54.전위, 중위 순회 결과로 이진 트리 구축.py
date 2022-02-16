from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> [TreeNode]:
        if inorder:
            # 현재 inorder의 루트값을 뽑자
            index = inorder.index(preorder.pop(0))
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder,inorder[:index])
            node.right = self.buildTree(preorder,inorder[index+1:])
            return node
        return None

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
a = Solution().buildTree(preorder,inorder)