class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(2.5)
l1.next.next.next = ListNode(3)
l1.next.next.next.next = ListNode(4)
l1.next.next.next.next.next = ListNode(5)
a = Solution().reverseList(l1)
while a:
    print(a.val, "->",end ="")
    a = a.next