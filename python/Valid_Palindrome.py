import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^0-9a-zA-Z\s]+","",s)
        s = s.replace(" ","")
        s = s.lower()
        print (s)
        return s == s[::-1]
        
