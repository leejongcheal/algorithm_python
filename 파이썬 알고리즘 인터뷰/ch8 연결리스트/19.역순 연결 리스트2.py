class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head:ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head
        root = start = ListNode()
        root.next = head
        for _ in range(left - 1):
            start = start.next
        end = start.next
        start = start
        for _ in range(right - left):
            temp, end.next, start.next = start.next, end.next.next, end.next
            start.next.next = temp
        return root.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
a = Solution().reverseBetween(l1,2,4)
while a:
    print(a.val, "->",end ="")
    a = a.next