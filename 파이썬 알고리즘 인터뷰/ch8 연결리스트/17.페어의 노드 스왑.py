class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode):
        # cur = head
        # while cur and cur.next:
        #     cur.val, cur.next.val = cur.next.val, cur.val
        #     cur = cur.next.next
        # return head
        root = prev = ListNode()
        prev.next = head
        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head
            # a전의 노드들을 연결해주기 위함
            prev.next = b
            # next.next가 아닌걸 주의
            head = head.next
            prev = prev.next.next
        return root.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
a = Solution().swapPairs(l1)
while a:
    print(a.val, "->",end ="")
    a = a.next