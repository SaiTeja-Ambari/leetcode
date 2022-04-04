class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = min(nums)
        s=0
        for i in nums:
            s+=i
            if(s>maxi):
                maxi=s
            if(s<0):
                s=0
        return maxi
            
        
