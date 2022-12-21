class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        forward_counter = 0
        backward_counter = len(s) - 1

        while backward_counter > forward_counter:
            if not s[backward_counter].isalnum():
                backward_counter -= 1
            elif not s[forward_counter].isalnum():
                forward_counter += 1
            elif s[forward_counter].lower() != s[backward_counter].lower():
                return False
            else:
                forward_counter += 1
                backward_counter -= 1
        return True
