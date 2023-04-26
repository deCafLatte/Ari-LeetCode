class Solution(object):
    def createTargetArray(self,nums, index):
        self=[]
        for i in range(len(index)): 
            self.insert(index[i],nums[i])
        return self
