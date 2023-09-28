class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = [i*i for i in nums]
        return sorted(squared)
