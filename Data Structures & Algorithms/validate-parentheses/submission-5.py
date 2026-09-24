class Solution:
    def isValid(self, s: str) -> bool:

        stak = [s[0]]

        for c in s[1:]:
            if stak and stak[-1] + c in ["()", "[]", "{}"]:
                stak.pop()
            else:
                stak.append(c)

        return not bool(stak)
                
 
        