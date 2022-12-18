class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                else:
                    top = stack.pop()
                    if (top == '(' and ch != ')') or (top == '[' and ch != ']') or (top == '{' and ch != '}'):
                        return False

        return len(stack) == 0
