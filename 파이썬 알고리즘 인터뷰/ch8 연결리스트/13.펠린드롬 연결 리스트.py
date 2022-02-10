# https://leetcode.com/problems/palindrome-linked-list/submissions/  에서 실행해야함
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 러너를 이용한 풀이
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            # rev = slow를 해버리면 나중에
            # rev값이 변경되면 slow도 같이 변경되는 개같은 파이썬의특징이 있음 p212참고
            rev, rev.next, slow = slow, rev, slow.next
        # 짝수인경우 fast는 None(tail.next값인)의 값을 가짐
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            rev, slow = rev.next,slow.next
        return not rev
        # q = deque()
        # if not head:
        #     return 1
        # node = head
        # while node is not None:
        #     q.append(node.val)
        #     node = node.next
        # # q == q[::-1] 보다 20%정도 빠름
        # while q:
        #     if q.popleft() != q.pop():
        #         return 0
        # return 1