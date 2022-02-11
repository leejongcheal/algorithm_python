from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 종료조건을 일부로줌
        if not l1 and not l2:
            return None
        # l1이 없으면 l2의 값을 주고, 둘다 있으면 l2값이 l1보다 작은경우 l1이 작은값을 가지도록함
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        # l1에 값이 없다면 l2에도 없다는 뜻이니 끝나야함
        # l1에 값이 있다면 더 돌아야함
        if l1:
            # l1.next에는 l1.next or l2중 작은값이 들어감
            # 실제 코드에서는 뒤에 연결리스트까지 정렬된 상태의 연결리스트가 들어감
            # ex) l1 1->2->3 일때 l1.next 에 1->2->3->4->4 가 들어가서
            # l1 1->   1->2->3->4->4 가 됨
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1

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