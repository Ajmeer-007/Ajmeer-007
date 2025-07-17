class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s= "".join(ch for ch in s if ch.isalnum())
        s=s.lower()
        b= s[::-1]
        if s== b:
            return True
        else:
            return False
        '''s = "".join(c.lower() for c in s if self.alphanumeric(c))
        return (s == s[::-1])

    def alphanumeric(self,s):
        return ('a'<= s <='z')or('A'<=s<='Z')or('0'<=s<='9')'''
