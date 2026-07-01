class Solution:
    def computeLPS(self, pattern:str):
        lps = [0]*len(pattern)
        length = 0

        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length+=1
                lps[i] = length
                i+=1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i+=1

        return lps


    def KMP(self, text:str, pattern:str):
        lps = self.computeLPS(pattern)

        result = []
        i = j = 0

        while i < len(text):

            if text[i] == pattern[i]:
                i+=1
                j+=1
            if j == len(pattern):
                result.append(i - j)
                j = lps[j - 1]
            elif i < len(text) and text[i] != pattern[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i+=1

        return result


sol = Solution()
text = "ababcababcabc"
pattern = "abc"
print("Pattern found at indices:", sol.KMP(text, pattern))