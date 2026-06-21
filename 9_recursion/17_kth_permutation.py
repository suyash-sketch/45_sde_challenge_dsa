class Solution:
    
    def get_permutation(self, n, k):
        fact = 1
        numbers = []

        for i in range(1, n):
            fact*=i
            numbers.append(i)
        numbers.append(n)

        ans = ""
        k -=1

        while numbers:
            ans += str(numbers[k//fact])
            numbers.remove(numbers[k//fact])
            if not numbers:
                break

            k= k% fact

            fact = fact // len(numbers)

        return ans

n = 3
k = 3

sol = Solution()
answer = sol.get_permutation(n, k)
print(answer)
