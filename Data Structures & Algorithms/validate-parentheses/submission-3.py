class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ref = {'(':')', '{':'}', '[': ']'}
        if (len(s)%2 != 0):
            return False
        for char in s:
            if (char == '(' or char == '{' or char == '['):
                stack.append(char)
            elif (len(stack) == 0 or char != ref[stack.pop()]):
                return False
        if (len(stack) > 0):
            return False            
        return True