class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            letters = {}
            for char in s:
                if char in letters.keys():
                    letters[char] += 1
                else:
                    letters[char] = 1
            
            for char in t:
                if char in letters.keys():
                    if letters[char] > 0:
                        letters[char] -= 1
                    else:
                        return False
                else:
                    return False

            return True
        return False