from collection import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        for k,v in freq.items():
            if v > len(nums)//2:
                return k
        
