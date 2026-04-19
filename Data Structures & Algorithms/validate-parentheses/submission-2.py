class Solution:
    def isValid(self, s: str) -> bool:
        # parentheses = index 0, curly = index 1, and square = index 2
        curr_bracket = []
        
        for elem in s:
            if elem == '(':
                curr_bracket.append(0)
            elif elem == '{':
                curr_bracket.append(1)
            elif elem == '[':
                curr_bracket.append(2)
            else:
                if len(curr_bracket) == 0:
                    return False
                elif elem == ')':
                    if curr_bracket.pop(-1) != 0:
                        return False
                elif elem == '}':
                    if curr_bracket.pop(-1) != 1:
                        return False
                elif curr_bracket.pop(-1) != 2:
                    return False
        
        if len(curr_bracket) == 0:
            return True
        return False
