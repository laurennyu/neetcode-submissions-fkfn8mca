class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = {}
        for char in s1:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

        i, j = 0, 0
        while j < len(s2):
            curr_char = s2[j]
            if curr_char in counts:
                if counts[curr_char] > 0:
                    counts[curr_char] -= 1
                else:
                    # Move i to the index after the first occurence of curr_char
                    while s2[i] != curr_char:
                        counts[s2[i]] += 1
                        i += 1
                    i += 1

                # Check if substring is found
                if j - i + 1 == len(s1):
                    return True

            else:
                # Move i and j after the current position of j 
                # (the substring cannot include this char)
                while i < j:
                    counts[s2[i]] += 1
                    i += 1
                i += 1

            j += 1
        
        return False