class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        i = 0
        p1 = 0
        p2 = 0
        maxi = 1
        l = -1
        r = 1
        while (i < n - 1):
            p1 = i
            p2 = i + 1
            while (p1 >= 0 and p2 < n and s[p1] == s[p2]):
                p1 -= 1
                p2 += 1
            # print(p1+1,p2-1)
            if (p2 - p1 - 1 > maxi):
                maxi = p2 - p1 - 1
                l = p1
                r = p2
            p1 = i - 1
            p2 = i + 1
            while (p1 >= 0 and p2 < n and s[p1] == s[p2]):
                p1 -= 1
                p2 += 1
            # print(p1+1,p2-1)
            if (p2 - p1 - 1 > maxi):
                maxi = p2 - p1 - 1
                l = p1
                r = p2

            i += 1
        return (s[l + 1:r])