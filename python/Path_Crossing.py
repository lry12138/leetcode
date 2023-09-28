class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0
        past = defaultdict(int)
        past[(0,0)] = 1
        count = 0
        for p in path:
            count += 1
            if p == 'N':
                y += 1
            elif p == 'S':
                y -= 1
            elif p == 'E':
                x += 1
            elif p == 'W':
                x -= 1
            loc = (x,y)
            # check existance
            if past[loc] == 1 :
                return True
            else: 
                past[loc] += 1

        return False
