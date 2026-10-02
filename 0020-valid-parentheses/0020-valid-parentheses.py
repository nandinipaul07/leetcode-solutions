class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []

        pair = {
            ")": "(", 
            "]": "[",
            "}": "{",
        }

        for char in s:
            if char in "([{":
                stack.append(char)

            else:
                if not stack or stack[-1] != pair[char]:
                    return False

                stack.pop()

        return len(stack) == 0
