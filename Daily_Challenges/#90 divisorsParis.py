from itertools import combinations
def divisorsPairs(s):
        s.sort()
        res = 0
        pairs = combinations(s, 2)
        for i in pairs:
                if i[-1]%i[0] == 0:
                        res += 1
        return res
                