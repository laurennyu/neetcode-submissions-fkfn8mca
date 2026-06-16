class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Let valid_word[i] be a boolean indicating if the substring of s from
        # 0 to i is composed of valid words
        valid_word = [0] * (len(s) + 1)
        valid_word[0] = 1 # Base case- empty string does not contradict word dict

        for i in range(1, len(s)+1):
            for j in range(i):
                if valid_word[j] and s[j:i] in wordDict:
                    valid_word[i] = 1
                    break

        return bool(valid_word[-1])