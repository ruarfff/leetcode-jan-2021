from typing import List


class Solution1:
    def canPermutePalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        char_counts = {}
        for c in s:
            if c in char_counts:
                char_counts[c] = char_counts[c] + 1
            else:
                char_counts[c] = 1
        values = char_counts.values()
        num_odd = 0

        for n in values:
            if n == 1 or n % 2 != 0:
                num_odd += 1

        return num_odd < 2


class Solution2:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        index = 0
        new_index = index
        pieces_m = pieces
        while index < len(arr):
            curr = arr[index]            
            for a in pieces_m:                
                if a[0] == curr and a == arr[index : index + len(a)]:
                    new_index += len(a)
                    pieces_m.remove(a)
            if new_index == index:
                return False
            else:
                index = new_index
        return True
