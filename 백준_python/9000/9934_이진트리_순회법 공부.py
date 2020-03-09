def inorder(i):
    if 2*i < 2**k and Tree[2*i] == 0:
        inorder(2*i)
    Tree[i] = q.pop(0)
    if 2*i+1 < 2**k and Tree[2*i+1] == 0:
        inorder(2*i+1)


k = int(input())
Tree = [0]*(2**k)
q = input().split()
inorder(1)
for i in range(0,k):
    print(" ".join(Tree[2**i:2**(i+1)]))


