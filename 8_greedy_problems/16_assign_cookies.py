class Solution:
    def find_content_children(self,children: list[int], cookie:list[int]):
        children.sort()
        cookie.sort()

        children_index = 0
        cookie_index = 0

        while children_index < len(children) and cookie_index < len(cookie):
            if cookie[cookie_index] >= children[children_index]:
                children_index+=1

            cookie_index+=1

        return children_index


sol = Solution()
children = [1,2,3]
cookie = [1,1]

answer = sol.find_content_children(children, cookie)
print(answer)
