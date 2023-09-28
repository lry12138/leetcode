class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(nums[i]+prefix[i-1])
        
        total = prefix[-1]

        if total == prefix[0]:
            return 0 

        for j in range(1, len(prefix)):
            if total- prefix[j] == prefix[j-1]:
                return j

        

        return -1
