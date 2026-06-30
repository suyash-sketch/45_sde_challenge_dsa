class Solution:
    def longestCommonSequence(self, strs: list[str]):
        if not strs:
            return ""

        strs.sort()

        first = strs[0]
        last = strs[-1]
        ans = []

        for i in range(min(len(first), len(last))):

            if first[i] != last[i]:
                return ''.join(ans)

            ans.append(first[i])


        return ''.join(ans)