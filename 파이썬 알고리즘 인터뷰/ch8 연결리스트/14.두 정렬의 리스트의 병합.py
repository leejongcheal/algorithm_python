from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = now = ListNode()
        head1, head2 = l1, l2
        while head1 is not None and head2 is not None:
            if head1.val <= head2.val:
                now.next = head1
                head1 = head1.next
            else:
                now.next = head2
                head2 = head2.next
            now = now.next
        while head1 is not None:
            now.next = head1
            head1 = head1.next
            now = now.next
        while head2 is not None:
            now.next = head2
            head2 = head2.next
            now = now.next
        return root.next




l1 = ListNode(1)
l1.next= ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

s = Solution()
answer = s.mergeTwoLists(l1, l2)
while answer is not None:
    print(f'{answer.val} ->', end=" ")
    answer = answer.next