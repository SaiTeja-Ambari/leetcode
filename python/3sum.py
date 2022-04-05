class Solution:
    def threeSum(self, a: List[int]) -> List[List[int]]:
        n=len(a)
        if(n<3):
            return []
        a.sort()
        ans=[]
        s=set()
        for i in range(n-2):
            j=i+1
            k=n-1
            while(j<k):
                if(a[i]+a[j]+a[k] == 0):
                    if((a[i],a[j],a[k]) not in s):
                        ans.append([a[i],a[j],a[k]])
                        s.add((a[i],a[j],a[k]))
                    j+=1
                    k-=1
                elif(a[i]+a[j]+a[k]>0):
                    k-=1
                elif(a[i]+a[j]+a[k]<0):
                    j+=1
        return ans




