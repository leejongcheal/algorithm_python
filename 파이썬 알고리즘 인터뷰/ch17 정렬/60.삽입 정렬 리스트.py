class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: [ListNode]) ->[ListNode]:
        if not head:
            return None
        # cur 정렬을 끝난 대상으로 , head를 정렬해야할 대상으로
        cur = parent = ListNode(None)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            cur.next, head.next, head = head, cur.next, head.next
            # if head and cur.val > head.val:
            cur = parent
        return parent.next

root = ListNode(3)
root.next = ListNode(1)
root.next.next = ListNode(4)
root.next.next.next = ListNode(2)
a = Solution().insertionSortList(root)
print(1)

