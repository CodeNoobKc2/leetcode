from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        tot = 1
        cur = head
        virtual = ListNode(-1,next=head)
        indexed:List[ListNode] = [virtual]
        while cur != None:
            tot = tot + 1
            indexed.append(cur)
            cur = cur.next


        target = indexed[tot-n]
        pre = indexed[tot-n-1]
        # remove target node
        pre.next = target.next
        return virtual.next
