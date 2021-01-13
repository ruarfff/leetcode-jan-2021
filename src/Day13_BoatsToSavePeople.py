from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        i = 0
        j = len(people) - 1
        while i <= j:
            i = i + 1 if people[i] + people[j] <= limit else i
            boats += 1
            j -= 1
        return boats