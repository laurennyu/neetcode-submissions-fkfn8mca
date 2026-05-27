class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_chars = [char for char in s.lower() if ('a' <= char <= 'z') or ('0' <= char <= '9')]
        clean = ''.join(clean_chars)

        return clean == ''.join(reversed(clean_chars))