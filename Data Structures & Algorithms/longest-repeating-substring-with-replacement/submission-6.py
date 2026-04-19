class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window but you also have k strikes
        i = 0
        max_len = 1
        
        j = 1
        remaining_strikes = k
        while j < len(s):
            if s[j] == s[i]:
                j += 1
            elif remaining_strikes > 0:
                remaining_strikes -= 1
                j += 1
            else:
                # Out of strikes, no longer a viable substring
                max_len = max(max_len, j - i)
                # Move i to be a different character value
                while s[i + 1] == s[i]:
                    i += 1
                i += 1
                # Move j too
                j = i + 1
                # Refresh the remaining strikes
                remaining_strikes = k

            if j >= len(s) and i < len(s) - 1:
                # Out of string, no longer a viable substring
                max_len = max(max_len, min(len(s), j - i + remaining_strikes))
                # Move i to be a different character value
                while i < len(s) - 1 and s[i + 1] == s[i]:
                    i += 1
                i += 1
                # Move j too
                j = i + 1
                # Refresh the remaining strikes
                remaining_strikes = k
        
        # If remaining strikes at end of string, add to len (if chars available)
        max_len = max(max_len, min(len(s), j - i + remaining_strikes))

        return max_len