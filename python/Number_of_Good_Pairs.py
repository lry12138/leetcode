class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        c = defaultdict(list)
        for i in range(len(nums)):
                c[nums[i]].append(i) 

        for k,v in c.items():
            for i in range(len(v)):
                count += i

        return count
