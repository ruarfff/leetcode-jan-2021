class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 0:
            return 0
        # Setup space to count [a, e, i, o, u] initialized with 1
        counts = [1] * 5

        # Let's do this n - 1 times basically
        # Note if n == 1, count will be 5 and this loop is skipped
        while n > 1:
            n -= 1
            # For each possible vowel
            for i in range(1, len(counts)):
                # Take the first iteration as an example where n == 2.
                # Conceptually we start with [a = 1, e = 2, i = 1, o = 1, u = 1]
                # Take i = 0. After counts[i] += counts[i - 1] we get [a = 1. e = 2, i = 4, o = 4, u = 5]
                # And so on until we get [a = 1, e = 2, i = 3, o = 4, u = 5]
                # Sum that you get 15
                # ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"]
                # Note the characteristic ot this. The numbers for each letter correspond to how many strings end with that letter.
                # Because 'a' is lexicographically the smallest, only one string can end with it "aa". Because u is the largest, the greatest number of strings end with it.
                counts[i] += counts[i - 1]

        return sum(counts)