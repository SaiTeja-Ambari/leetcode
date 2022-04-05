# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p = list1
        q = list2
        ans = ListNode(0)
        ptr = ans
        while (p and q):
            if (p.val <= q.val):
                ptr.next = ListNode(p.val)
                ptr = ptr.next
                p = p.next
            else:
                ptr.next = ListNode(q.val)
                ptr = ptr.next
                q = q.next
        if (p):
            ptr.next = p
        if (q):
            ptr.next = q

        return ans.next
