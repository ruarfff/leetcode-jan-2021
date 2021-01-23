from typing import List


class Solution:
    def sort(self, mat, x, y):
        current_diag = []
        while x < len(mat) and y < len(mat[0]):
            current_diag.append(mat[x][y])
            x += 1
            y += 1
        current_diag.sort()
        while x > 0 and y > 0:
            x -= 1
            y -= 1
            mat[x][y] = current_diag.pop()

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # For each diagonal in the matrix starting at the bottom left
        for i in range(len(mat)):
            self.sort(mat, i, 0)
        # For each diagonal in the matrix starting at the top right
        for i in range(len(mat[0])):
            self.sort(mat, 0, i)

        return mat