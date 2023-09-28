class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # list the cost to switch each letter
        cost_list = [abs(ord(s[i])-ord(t[i])) for i in range(len(s))]
        
        l = r = ans = 0
        total = 0 
        while r < len(s):
            if total + cost_list[r] <= maxCost:
                total = total + cost_list[r]
                r += 1
            else:
                total = total-cost_list[l]
                l += 1
            if ans < r-l:
                ans = r-l
        return ans
        
