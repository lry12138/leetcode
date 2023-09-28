class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        l = 0
        count = 0 
        #s_list = [w for w in s]
        for w in s[l:k]:
            if w in vowels:
                count += 1
        ans = count 
        for r in range(k,len(s)):
            if s[l] in vowels:
                count -= 1 

            if s[r] in vowels:
                count += 1 
            if ans <count:
                ans = count 

            l += 1

        return ans
