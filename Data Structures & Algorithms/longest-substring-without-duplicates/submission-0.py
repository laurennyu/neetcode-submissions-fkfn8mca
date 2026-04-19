class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        i = 0
        seen = {s[0]}
        max_len = 1

        j = 1
        while j < len(s):
            # Assess substring validity
            if s[j] not in seen:
                seen.add(s[j])
                j += 1
            else:
                # Substring no longer valid
                max_len = max(max_len, j-i)
                # Update pointers
                while s[i] != s[j]:
                    seen.remove(s[i])
                    i += 1
                # Now, s[i] == s[j]
                i += 1
                j += 1

        max_len = max(max_len, j-i)

        return max_len