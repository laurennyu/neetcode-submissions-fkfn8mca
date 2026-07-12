class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_chars = {}
        for char in s1:
            if char in s1_chars:
                s1_chars[char] += 1
            else:
                s1_chars[char] = 1
        
        chars_needed = s1_chars.copy()
        i = 0
        j = 0
        while j < len(s2):
            new_char = s2[j]
            if new_char in chars_needed:
                if chars_needed[new_char] > 0:
                    # Take this char and widen 
                    chars_needed[new_char] -= 1

                    if j - i + 1 == len(s1):
                        return True
                else:
                    # Slide i forward until we can take j
                    while s2[i] != new_char:
                        chars_needed[s2[i]] += 1
                        i += 1
                    i += 1
                j += 1
            else:
                # We can't take this char regardless. Restart the window
                i = j + 1
                j = i
                chars_needed = s1_chars.copy()

            print(s2[i:j+1])
        return False