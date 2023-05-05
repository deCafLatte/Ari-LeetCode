class Solution(object):
    def missingNumber(self, nums):
        list1=[0]
        
        nums.sort()
        for i in range(int(nums[-1])):
            list1.append(i)
        list2=[i for i in list1 if i not in nums]
        b=int(list2[0])
        return(b)
