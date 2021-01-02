from typing import List


class Solution:
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
