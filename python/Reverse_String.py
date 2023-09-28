class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s)-1
        while l < r:
            a = s[l]
            b = s[r]
            #swap letters
            s[l] = b
            s[r] = a
            
            #move pointers
            l +=1
            r -= 1
            
        return s
            
