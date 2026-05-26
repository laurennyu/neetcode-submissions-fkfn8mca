class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        # set up 2D array; will be filled with booleans
        is_palindrome = []
        for i in range(len(s)):
            row = [0] * len(s)
            row[i] = True
            if i > 0:
                row[i-1] = True
            is_palindrome.append(row)

        max_pal_i = 0
        max_pal_j = 0
        max_len = 1

        # Recursive case
        for i in range(len(s)-2, -1, -1):
            for j in range(i+1, len(s)):
                is_pal = (s[i] == s[j]) and is_palindrome[i+1][j-1]
                if is_pal and j-i > max_pal_j-max_pal_i:
                    max_pal_i = i
                    max_pal_j = j
                is_palindrome[i][j] = is_pal

        return s[max_pal_i:max_pal_j+1]
