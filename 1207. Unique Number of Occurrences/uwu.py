class Solution(object):
    def uniqueOccurrences(self, arr):
        qwq=[]
        quq=[]
        arr.sort()
        print("arr=",arr)
        qaq=set(arr)
        print("qaq=",qaq)
        qaq=[ int(x) for x in qaq ]     #qaq含有arr的不重复字符串eg（1，2，3）
        for i in range(len(qaq)):
            #print("qaq[i]=",qaq[i])
            j=arr.index(qaq[i])
            #print("j=",j)
            quq.append(j)
            #print("quq=",quq)  #quq含有arr中1，2，3，4，5的下标
        for i in quq: 
            #print("i=",i)
            qwq.append(arr.count(arr[i-1]))
            #print("qwq=",qwq)                                                                                              
        qwq.sort()

        a=0
        for i in range(len(qwq)-1):
            if (qwq[i+1]-qwq[i])==0:
                a=a+1#不知道为什么就是想暴力写一遍quq 大概用了1.5h修改 感觉毫无意义啊喂！！
