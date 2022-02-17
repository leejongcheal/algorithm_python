class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: [ListNode]) -> [ListNode]:
        if not head:
            return None
        L = []
        while head:
            L.append(head.val)
            head = head.next
        L.sort()
        head = root = ListNode(L[0])
        for i in range(len(L) - 1):
            head.next = ListNode(L[i+1])
            head = head.next
        return root