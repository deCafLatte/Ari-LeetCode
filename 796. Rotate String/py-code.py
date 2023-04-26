class Solution(object):
    def rotateString(self, s, goal):
        if len(s)!=len(goal):
            return False
        else:
            if goal in s+s:
                return True
            else:
                return False
                
  '''
  All rotations of A are contained in A+A. Thus, we can simply check whether B is a substring of A+A. We also need to check A.length == B.length, otherwise we will fail cases like A = "a", B = "aa".
  
  class Solution(object):
      def rotateString(self, A, B):
          return len(A) == len(B) and B in A+A
  
  '''
