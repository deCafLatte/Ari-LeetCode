class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        maxnum=float("inf")
        qwq=[]
        for i in range(len(arr)-1):
            minnum=arr[i+1]-arr[i]
            if minnum==maxnum:
                qwq.append([arr[i],arr[i+1]])
            elif minnum < maxnum:
                qwq=[[arr[i],arr[i+1]]]
                maxnum=minnum
        return qwq
             
