from collections import defaultdict,Counter
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        c = collections.Counter(nums)

        ans = - 1
        for n in c:
            if c[n] == 1:
                if ans < n:
                    ans = n
        
        return ans
