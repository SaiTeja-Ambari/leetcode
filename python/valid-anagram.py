class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1=len(s)
        n2=len(t)
        if(n1!=n2):
            return False
        d1=[0]*26
        for i in s:
            d1[ord(i)-97]+=1
        for i in t:
            d1[ord(i)-97]-=1
            if(d1[ord(i)-97]<0):
                return False
        for i in d1:
            if(i!=0):
                return False
        return True