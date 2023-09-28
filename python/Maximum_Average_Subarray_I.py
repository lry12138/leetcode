class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = ans = sum(nums[:k])
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            if ans < curr:
                ans = curr

        return ans/k
