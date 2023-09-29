class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        ans = 0
        while r<len(prices):
            curr = prices[r]-prices[l]
            if curr > 0:
                if ans < curr:
                    ans = curr

            else:
                l = r
            r += 1
            
        return ans
