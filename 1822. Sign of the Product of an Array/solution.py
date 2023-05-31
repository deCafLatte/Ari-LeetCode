class Solution(object):
    def arraySign(self, nums):
        b=0
        for a in nums:
            if a<0:
                b=b+1
        if 0 in nums:
            return 0

        elif b%2==0:
            return 1
        elif b%2==1:
            return -1
