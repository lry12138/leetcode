class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # covert s to list 
        # initalise two pointer on at 0 the other at one end 
        # check if both pointer is at english alphabets
        s_list = list(s)
        l = 0
        r = len(s)-1  
        while l < r :
            letter1 = s_list[l]
            letter2 = s_list[r]
            if letter1.isalpha() and letter2.isalpha():
                s_list[l] = letter2
                s_list[r] = letter1
                l += 1
                r -= 1

            elif letter1.isalpha():
                r -= 1

            else:
                l += 1
            
            
        return ''.join(s_list)
