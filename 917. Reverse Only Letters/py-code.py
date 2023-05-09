class Solution(object):
    def wordSubsets(self, words1, words2):
        a=1
        b=set(words1)
        c={}
        for i in words2:
          for j in i:
            count=i.count(j)
            if j not in c or count > c[j]:
              c[j]=count
        for i in words1:
          for j in c:
            if i.count(j)<c[j]:
              b.remove(i)
              break 
        return(b)
