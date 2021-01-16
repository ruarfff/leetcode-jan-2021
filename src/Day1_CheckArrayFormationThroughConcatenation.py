from typing import List


class Solution:
    # The goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].
    # Return true if it is possible to form the array arr from pieces. Otherwise, return false.
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # Setup 2 pointers. One to iterate over arr
        # The other pointer slides along with the pieces
        index = 0
        new_index = index

        # We won't always iterate over every bit of arr so using a while to track index that gets updated in the loop.
        while index < len(arr):
            # Let's look at each piece and see if it matches a part of arr
            for piece in pieces:
                current_piece_length = len(piece)
                # Check if the piece matches a section of arr from the current index.
                # Example. if i = 0, arr = [1,2,3], piece = [1,2] then we would have a match and new_index would jump to 2 i.e. 0 + len(piece)
                # Checking piece[0] == arr[index] is just a performance optimisation so we don't always check the full piece unnecessarily
                if (
                    piece[0] == arr[index]
                    and piece == arr[index : index + current_piece_length]
                ):
                    new_index += current_piece_length
                    # We don't want to count this piece again so remove it
                    pieces.remove(piece)
            # If at any point we have not found a matching piece we must return false
            if new_index == index:
                return False
            else:
                # Move the index in arr up to new_index to continue our matching from there
                index = new_index
        # We only get here if we successfully matched all pieces in the array
        return True
