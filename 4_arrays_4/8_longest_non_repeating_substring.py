S = "abcddabac"

class Solution:
    """ Function to find the longest substring
        without repeating characters """
    def longestNonRepeatingSubstring(self, s):
        n = len(s)

        hashlen = 256

        hash_table = [-1]*hashlen

        for i in range(hashlen):
            hash_table[i] = -1

        l = 0
        r = 0
        maxlen = 0

        while r < n:
            if hash_table[ord(s[r])] != -1:
                l = max(hash_table[ord(s[r])] + 1, l)
            
            curent_len = r - l + 1

            maxlen = max(curent_len, maxlen)

            hash_table[ord(s[r])] = r

            r+=1

        return maxlen


sol = Solution()

answer = sol.longestNonRepeatingSubstring(S)
print(answer)