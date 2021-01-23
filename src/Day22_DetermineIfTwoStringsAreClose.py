def count_chars_map(word: str):
    counts = {}
    for c in word:
        if c in counts:
            counts[c] = counts[c] + 1
        else:
            counts[c] = 1
    return counts


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1l = len(word1)
        w2l = len(word2)
        if w1l != w2l:
            return False
        w1_counts = count_chars_map(word1)
        w2_counts = count_chars_map(word2)

        if sorted(list(w1_counts.keys())) != sorted(list(w2_counts.keys())):
            return False

        return sorted(list(w1_counts.values())) == sorted(list(w2_counts.values()))
