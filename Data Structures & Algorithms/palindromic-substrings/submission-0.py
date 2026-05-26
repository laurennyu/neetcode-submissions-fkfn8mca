class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1

        # set up 2D array; will be filled with booleans
        is_palindrome = []
        pal_count = len(s)
        for i in range(len(s)):
            row = [0] * len(s)
            row[i] = True
            if i > 0:
                row[i-1] = True
            is_palindrome.append(row)

        # Recursive case
        for i in range(len(s)-2, -1, -1):
            for j in range(i+1, len(s)):
                is_pal = (s[i] == s[j]) and is_palindrome[i+1][j-1]
                if is_pal:
                    pal_count += 1
                is_palindrome[i][j] = is_pal

        return pal_count
