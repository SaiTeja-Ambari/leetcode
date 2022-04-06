"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if (root is None):
            return root
        q = []
        q.append(root)
        while (q):
            n = len(q)
            prev = None
            while (n > 0):
                cur = q.pop(0)
                n -= 1
                # print(cur.val)
                if (cur.left):
                    q.append(cur.left)
                if (cur.right):
                    q.append(cur.right)
                if (prev != None):
                    prev.next = cur
                prev = cur

            prev.next = None
        return root




