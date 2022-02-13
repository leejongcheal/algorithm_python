class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        odd_head, even_head = ListNode(), ListNode()
        odd, even = odd_head, even_head
        index = 1
        while head:
            if index%2 == 0:
                even.next = head
                even = even.next
            else:
                odd.next = head
                odd = odd.next
            head = head.next
            index += 1
        if odd.next is not None:
            odd.next = None
        if even.next is not None:
            even.next = None
        odd.next = even_head.next
        return odd_head.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
a = Solution().oddEvenList(l1)
while a:
    print(a.val, "->",end ="")
    a = a.next