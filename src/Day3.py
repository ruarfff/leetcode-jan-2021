def check(n: int, index: int, checking: dict) -> int:
    if index == 0:
        return 1
    total = 0

    for i in range(1, n + 1):
        if (i not in checking or not checking[i]) and (i % index == 0 or index % i == 0):
            checking[i] = True
            total += check(n, index - 1, checking)
            checking[i] = False
    return total


class Solution:
    def countArrangement(self, n: int) -> int:
        checking = {}
        return check(n, n, checking)
