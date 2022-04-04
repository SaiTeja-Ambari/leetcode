class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        #using 2 arrays
        # pre=[0]*n
        # post=[0]*n
        # pre[0]=nums[0]
        # post[-1]=nums[-1]
        # i=1
        # while(i<n):
        #     pre[i]=pre[i-1]*nums[i]
        #     post[n-i-1]=post[n-i]*nums[n-i-1]
        #     i+=1
        # ans=[0]*n
        # for i in range(1,n-1):
        #     ans[i]=pre[i-1]*post[i+1]
        # ans[0]=post[1]
        # ans[n-1]=pre[-2]
        # #print(pre,post)
        # return ans
        
        #using 1 array
        ans=[1]*n
        temp=1
        for i in range(n):
            ans[i]=temp
            temp*=nums[i]
        temp=1
        for i in range(n-1,-1,-1):
            ans[i]*=temp
            temp*=nums[i]
        return ans
