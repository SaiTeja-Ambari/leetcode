class Solution:
    def search(self, a: List[int], k: int) -> int:
        n=len(a)
        l=0
        r=n-1
        while(l<=r):
            m=(l+r)//2
            if(a[m]==k):
                return m
            if(a[l]<=a[m]):
                if(a[l]<=k and k<=a[m]):
                    r=m-1
                else:
                    l=m+1
            else:
                if(a[r]>=k and a[m]<=k):
                    l=m+1
                else:
                    r=m-1
        return(-1)
                
                
                
                
        
