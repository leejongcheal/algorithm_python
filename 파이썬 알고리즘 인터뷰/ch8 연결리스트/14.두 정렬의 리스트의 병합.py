from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head1, head2 = list1, list2
        res = ListNode(0)
        head_r = res
        while head1 and head2:
            if head1.val < head2.val:
                head_r.next = ListNode(head1.val)
                head1 = head1.next
            else:
                head_r.next = ListNode(head2.val)
                head2 = head2.next
            head_r = head_r.next
        while head1:
            head_r.next = ListNode(head1.val)
            head1 = head1.next
            head_r = head_r.next
        while head2:
            head_r.next = ListNode(head2.val)
            head2 = head2.next
            head_r = head_r.next
        return res.next


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