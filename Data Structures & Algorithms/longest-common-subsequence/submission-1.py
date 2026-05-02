class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 2D DP: let lcs[i][j] = longest common subsequence between
        # text1[0...i] and text2[0...j]

        # Base case
        row = [0] * len(text2)
        if text1[0] == text2[0]:
            row[0] = 1
        for j in range(1, len(text2)):
            if row[j - 1] or text1[0] == text2[j]:
                row[j] = 1
        lcs = [row]

        for i in range(1, len(text1)):
            row = [0] * len(text2)
            # Base case
            if lcs[i - 1][0] or text1[i] == text2[0]:
                row[0] = 1
            lcs.append(row)

            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    # Take both
                    lcs[i][j] = lcs[i-1][j-1] + 1
                else:
                    lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

        return lcs[-1][-1]