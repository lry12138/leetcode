class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix =[]
        sums = 0
        for num in nums:
            prefix.append(sums+num) 
            sums += num
        return prefix
