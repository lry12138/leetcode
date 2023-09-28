from collections import defaultdict,Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rN = collections.Counter(ransomNote)
        mG = collections.Counter(magazine)
        for l in rN:
            if l not in rN or rN[l] > mG[l]:
                return False
        return True
