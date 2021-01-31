from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(map(str, word1)) == "".join(map(str, word2))

    def arrayStringsAreEqual2(self, word1: List[str], word2: List[str]) -> bool:
        w1, i, w1n = 0, 0, len(word1)
        w2, j, w2n = 0, 0, len(word2)

        while w1 < w1n and w2 < w2n:
            if word1[w1][i] != word2[w2][j]:
                return False
            if len(word1[w1]) - 1 > i:
                i += 1
            else:
                w1 += 1
                i = 0

            if len(word2[w2]) - 1 > j:
                j += 1
            else:
                w2 += 1
                j = 0
        return w1 + w2 == w1n + w2n
