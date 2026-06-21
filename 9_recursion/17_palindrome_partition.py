class Solution:
    def is_palindrome(self, s:str, left:int, right: int):
        while left < right:
            if s[left] != s[right]:
                return False
            left+=1
            right-=1

        return True

    def backtrack(self, index:int, s:str, ans: list[list[int]], arr: list[int]):
        if index == len(s):
            ans.append(arr[:])
            return

        for j in range(index, len(s)):
            if self.is_palindrome(s, index, j):
                substring = s[index:j+1] 
                arr.append(substring)
                self.backtrack(j +1, s, ans, arr)
                arr.pop()


    def partition(self, s: str):
        ans = []
        arr = []
        self.backtrack(0,s,ans, arr)
        return ans


sol = Solution()
s = "aabaa"
answer = sol.partition(s) 
print(answer)
