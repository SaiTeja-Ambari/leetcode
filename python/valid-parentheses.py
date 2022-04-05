class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        o=['(','{','[']
        for i in s:
            if(i in o):
                st.append(i)
            else:
                if(len(st)==0):
                    return(False)
                k=st.pop()
                if(k=='(' and i==')' or k=='{' and i=='}' or k=='[' and i==']'):
                    continue
                return(False)
        if(len(st)!=0):
            return(False)
        return(True)