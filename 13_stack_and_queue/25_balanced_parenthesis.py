class Solution:
    def __init__(self):
        self.stack = []
        
    def isValid(self, s: str):
        for ch in s:
            if ch in '({[':
                self.stack.append(ch) #push opening bracket to stack
            else:
                if not self.stack:
                    return False   # no matching opening bracket
                top = self.stack.pop()

                # check for matching pair 
                if (ch == ')' and top == '(') or (ch == '}' and top == '{') or (ch == ']' and top == '['):
                    continue
                else:
                    return False

        return not self.stack # true if all brackets matched
