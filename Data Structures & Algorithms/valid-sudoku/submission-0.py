class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Indexed by (j//3 * 3) + i//3
        seen_3x3 = []
        seen_col = []
        for dummy in range(9):
            seen_3x3.append(set())
            seen_col.append(set())

        for i in range(9):
            seen_row = set()
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    if num in seen_row or num in seen_col[j] or num in seen_3x3[(j//3 * 3) + i//3]:
                        return False
                    
                    seen_row.add(num)
                    seen_col[j].add(num)
                    seen_3x3[(j//3 * 3) + i//3].add(num)

        return True
