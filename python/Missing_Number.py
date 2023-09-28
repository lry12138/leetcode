class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        my_set = set(range(n+1))
        for num in nums:
            if num in my_set:
                my_set.remove(num)
                
        for k in my_set:
            return k
