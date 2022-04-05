class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        v = 31
        while (n > 0):
            r = n % 2
            ans += r << v
            v -= 1
            n //= 2
        return ans

