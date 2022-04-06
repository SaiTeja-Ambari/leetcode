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
        p = root
        p.next = None

        def get(p):
            temp = p.next
            while (temp):
                if (temp.left):
                    return temp.left
                if (temp.right):
                    return temp.right
                temp = temp.next
            return None

        while (p):
            q = p
            while (q):
                if (q.left):
                    if (q.right):
                        q.left.next = q.right
                    else:
                        q.left.next = get(q)
                if (q.right):
                    q.right.next = get(q)
                q = q.next
            if (p.left):
                p = p.left
            elif (p.right):
                p = p.right
            else:
                p = get(p)

        return root




