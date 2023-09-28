class Solution:
    def frequencySort(self, s: str) -> str:
        chars = collections.Counter(s)
        sorted_chrs = sorted(chars.items(), key=lambda x:x[1], reverse = True)
        ans = ""
        for k,v in sorted_chrs:
            ans += k*v
        return ans
