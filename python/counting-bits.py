class Solution:
    def countBits(self, n: int) -> List[int]:
        if (n == 0):
            return [0]
        elif (n == 1):
            return [0, 1]
        ans = [0, 1]
        for i in range(2, n + 1):
            if (i & i - 1 == 0):
                prev = i
                ans.append(1)
            else:
                ans.append(1 + ans[i - prev])
        return ans
