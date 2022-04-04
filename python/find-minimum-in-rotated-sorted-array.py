class Solution:
    def findMin(self, a: List[int]) -> int:
        n=len(a)
        l=0
        r=n-1
        if(n==1):
            return(a[0])
        if(n==2):
            return(min(a))
        if(a[l]<a[r] and a[l]<a[l+1]):
            return(a[l])
        if(a[r]<a[l] and a[r]<a[r-1]):
            return(a[r])
        
        while(l<=r):
            m=(l+r)//2
            if(a[m]>a[m+1]):
                return(a[m+1])
            if(a[m-1]>a[m]):
                return(a[m])
            if(a[m]>a[0]):
                l=m+1
            else:
                r=m-1
