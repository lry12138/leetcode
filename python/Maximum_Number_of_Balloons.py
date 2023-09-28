from collections import defaultdict, Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = collections.Counter(text)
        pos = []
        balloon = {'b':1,'a':1,'l':2,'o':2,'n':1} 
        for l in balloon:
            if l in c:
                pos.append(c[l]//balloon[l])
            else:
                pos.append(0)

        return min(pos)
