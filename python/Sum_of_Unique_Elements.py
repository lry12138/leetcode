class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dic = collections.Counter(nums)
        total = 0
        for k,v in dic.items():
            if v == 1:
                total += k
        return total
        
