class Solution(object):
    def isPalindrome(self, s):
            s=s.lower()
            strs = ''.join([x for x in s if x.isalpha()])
            rts =strs[::-1]
            if strs==rts:
                return True
            else:
                return False
