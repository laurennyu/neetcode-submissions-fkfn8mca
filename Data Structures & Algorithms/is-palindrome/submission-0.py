class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = s.lower()
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] not in alphanum:
                i += 1
                continue
            if s[j] not in alphanum:
                j -= 1
                continue
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False

        return True