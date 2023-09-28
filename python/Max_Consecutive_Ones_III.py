class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0 
        curr = 0
        ans = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                curr += 1
                    
            while curr > k:
                if nums[l] == 0:
                    curr -= 1 
                l += 1
            if ans <r-l+1:
                ans = r-l+1
        return ans
            
