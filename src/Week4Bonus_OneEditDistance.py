class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ls = len(s)
        lt = len(t)
        if abs(lt - ls) > 1:
            return False

        diffs = 0
        sp = 0
        tp = 0
        while sp < ls and tp < lt:
            if s[sp] != t[tp]:
                diffs += 1
                if diffs > 1:
                    return False
                if ls > lt or ls == lt:
                    sp += 1
                if ls < lt or ls == lt:
                    tp += 1
            else:
                sp += 1
                tp += 1

        if sp < ls or tp < lt:
            diffs += 1

        return diffs == 1