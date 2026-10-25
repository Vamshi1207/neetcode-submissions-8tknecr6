import heapq
from typing import List, Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 1. Push head of each non-empty list into min-heap
        heap = []
        for i, node in enumerate(lists):
            if node:
                # index breaks ties when values are equal
                heapq.heappush(heap, (node.val, i, node))

        # 2. Create dummy head to build merged list
        dummy = ListNode(0)
        cur = dummy

        # 3. Repeatedly extract smallest node and add its successor
        while heap:
            _, i, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        # 4. Return merged list starting after dummy
        return dummy.next
