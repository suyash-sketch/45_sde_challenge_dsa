
class Solution:
    def my_atoi(self, s: str):
        if not s:
            return 0

        # const for 32bit signed integer  range
        INT_MAX = 2**31 
        INT_MIN = -2**31 

        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i+=1

        if i == n:
            return 0

        # check for sign 
        sign= 1
        if s[i] == '+':
            i+=1
        elif s[i] == '-':
            sign=-1
            i+=1

        res = 0 
        while i < n and s[i].isdigit():
            digit = int(s[i])
            res = res * 10 + digit

            if sign*res <= INT_MIN:
                return INT_MIN
            if sign*res >= INT_MAX:
                return INT_MAX

            i+=1

        return res*sign


sol = Solution()
ans = sol.my_atoi("-91283472332")
print(ans)