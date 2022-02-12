import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: [ListNode]) -> [ListNode]:
        root = result = ListNode()
        heap = []
        """
        heap = [(1,4,5),(1,3,4),(2,6)]으로 넣어서 처음에 (1,4,5)중 1값만 사용후에 (4,5)를 다시 heap에
        넣는식으로 사용함 -> 나라면 1,4,5,1,3,4,2,6 으로 사용할려고 할텐데 신기하게 사용
        """
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]
            # r.next 힙에서 pop한 listNode[idx][now]...
            result = result.next
            # list[i]의 다음값이 있으면 heap에 값을 넣어준다.
            if result.next:
                heapq.heappush(heap,(result.next.val, idx, result.next))
        return root.next
# [[1,2,2],[1,1,2]]
"""
    heap에  1 4 5 1 3 4 2 6 순으로 넣어서 사용하는 경우에 
    원소로 now.val , i ,now를 쓰면 오류남 
    [[1,2,2],[1,1,2]] 의 경우 두번째 리스트 1,2번쨰에서 1,1,112 , 1,1,12 에서 112 와 12를 비교할수 없어서 오류남
    이를 위해서 index값을 따로 넣어서 풀이함 -> 위처럼 못풀 경우엔 이런식으로 예외를 생각해서 풀이할것
"""
# class Solution:
#     def mergeKLists(self, lists: [ListNode]) -> [ListNode]:
#         root = result = ListNode()
#         heap = []
#         for i in range(len(lists)):
#             now = lists[i]
#             index = 0
#             while now:
#                 heapq.heappush(heap,(now.val,i,index, now))
#                 now = now.next
#                 index += 1
#         while heap:
#             node = heapq.heappop(heap)
#             idx = node[1]
#             result.next = node[3]
#             result = result.next
#         return root.next



list = []
a = ListNode(1)
a.next = ListNode(4)
a.next.next = ListNode(5)
b = ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(4)
c = ListNode(2)
c.next = ListNode(6)
list.append(a)
list.append(b)
list.append(c)
answer = Solution().mergeKLists(list)
while answer:
    print(answer.val, "->", end=" ")
    answer = answer.next