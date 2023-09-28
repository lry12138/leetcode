class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 1
        while j < len(nums) :
            if nums[i]==0 and nums[j]!=0:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp  
                i+=1
                j+=1
            elif j<len(nums) and nums[j]==nums[i] and nums[i]==0 and nums[j]==0:
                j+=1
            else:
                i+=1
                j+=1
    
        
               
