class Solution(object):
    def moveZeroes(self, nums):
        for i in nums:
            if 0 in nums:
                nums.remove(0)
                nums.append(0)
