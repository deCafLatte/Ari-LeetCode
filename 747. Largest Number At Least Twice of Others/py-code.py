class Solution(object):
    def dominantIndex(self, nums):
        
        a=copy.deepcopy(nums)
        a.sort()
        if a[-1]>=(2*a[-2]):
            return (nums.index(a[-1]))
        else:
            return -1
