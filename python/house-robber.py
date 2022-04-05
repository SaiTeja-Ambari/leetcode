class Solution:
    def rob(self, nums: List[int]) -> int:
        m = -1
        n = len(nums)
        if (n < 2):
            return max(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            m = max(dp[i - 1], nums[i])
            dp[i] = max(m, dp[i - 2] + nums[i])
        return max(dp)
