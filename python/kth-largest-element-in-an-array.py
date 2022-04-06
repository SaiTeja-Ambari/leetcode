from heapq import heappush, heappop


class Solution:
    def findKthLargest(self, a: List[int], k: int) -> int:
        n = len(a)
        h = []
        for i in range(k):
            heappush(h, a[i])
        for i in range(k, n):
            if (a[i] > h[0]):
                heappop(h)
                heappush(h, a[i])
        return (h[0])
