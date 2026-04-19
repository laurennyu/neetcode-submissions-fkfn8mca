class Solution:
    def isValid(self, s: str) -> bool:
        # parentheses = index 0, curly = index 1, and square = index 2
        opens = [0] * 3
        curr_bracket = []
        
        for elem in s:
            if elem == '(':
                opens[0] += 1
                curr_bracket.append(0)
            elif elem == '{':
                opens[1] += 1
                curr_bracket.append(1)
            elif elem == '[':
                opens[2] += 1
                curr_bracket.append(2)
            elif elem == ')':
                if opens[0] > 0 and curr_bracket.pop(-1) == 0:
                    opens[0] -= 1
                else:
                    return False
            elif elem == '}':
                if opens[1] > 0 and curr_bracket.pop(-1) == 1:
                    opens[1] -= 1
                else:
                    return False
            elif opens[2] > 0 and curr_bracket.pop(-1) == 2:
                opens[2] -= 1
            else:
                return False
        
        if opens[0] + opens[1] + opens[2] == 0:
            return True
        return False
