class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        smallest = 0 
        sums = 0
        for num in nums:
            sums += num
            if sums <smallest:
                smallest = sums
        
        return 1-smallest
                
                    
