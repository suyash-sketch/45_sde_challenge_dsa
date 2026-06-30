import math

class Solution:
    def repeatedStringMatch(self, a: str, b: str):
        repeats = len(b) // len(a)
        count = 1
        
        while count <= repeats + 2:
            if b in a*count:
                return count
            else:
                count+=1
    
        return -1