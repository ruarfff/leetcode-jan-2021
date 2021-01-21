class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        stack = []
        brackets = {"}": "{", ")": "(", "]": "["}
        for b in s:
            if b in brackets:
                if len(stack) == 0 or stack.pop() != brackets[b]:
                    return False
            else:
                stack.append(b)

        return len(stack) == 0