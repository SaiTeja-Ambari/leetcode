class Solution:
    def maxArea(self, a: List[int]) -> int:
        m=0
        n=len(a)
        l=0
        r=n-1
        while(l<r):
            m=max(m,(min(a[l],a[r])*(r-l)))
            if(a[l]<a[r]):
                l+=1
            else:
                r-=1
        return(m)