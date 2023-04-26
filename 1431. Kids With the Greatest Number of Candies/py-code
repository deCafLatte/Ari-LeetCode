class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        list1=copy.deepcopy(candies)
        list1.sort()
        list2=[]
        
        
        for i in candies:
            if (i+extraCandies)>= list1[-1]:
                list2.append(bool(1))
            else:
                list2.append(bool(0))

        return list2
