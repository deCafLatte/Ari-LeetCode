class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        l=[]
        for i in licensePlate:
            if i.isalpha():
                l.append(i.lower())
        words.sort(key=len)
        for i in words:
            x=1
            for j in l:
                if (j not in i) or (l.count(j)>i.count(j)):
                    x=0
                    break
            
            if(x==1):
                return(i)
