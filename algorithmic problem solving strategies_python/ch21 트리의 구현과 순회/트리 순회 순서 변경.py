# 전위 중위가 주어질때 후위의 순서를 반환해야하는 문제
# 발상이 어려운데? 잘모르겠음
# 복잡한 분할정복 정도는 발상함 -> 이거네 짜는건 도 다른문제긴해 이게왜 난이도 하야 ㅋㅋ
import sys

def solve(preorder, inorder):
    global res
    n = len(preorder)
    if n == 0:
        return
    root = preorder[0]
    L = inorder.index(root)
    # 왼쪽
    solve(preorder[1:L+1], inorder[0:L])
    # 오른쪽
    solve(preorder[L+1:n], inorder[L+1:n])
    res.append(root)


read = sys.stdin.readline
for _ in range(int(read())):
    n = int(read())
    res = []
    preorder = list(map(int,read().split()))
    inorder = list(map(int,read().split()))
    solve(preorder, inorder)
    print(" ".join(map(str,res)))

