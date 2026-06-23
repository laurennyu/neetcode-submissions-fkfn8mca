class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        def search(i, j, idx):
            # i, j must be valid unseen coords, idx must be < len(word)
            nonlocal seen, board
            if board[i][j] == word[idx]:
                if idx == len(word) - 1:
                    return True # Found
                
                seen.add((i, j))
                
                if i > 0 and ((i-1, j) not in seen):
                    if search(i-1, j, idx+1):
                        return True
                if i < len(board)-1 and ((i+1, j) not in seen):
                    if search(i+1, j, idx+1):
                        return True
                if j > 0 and ((i, j-1) not in seen):
                    if search(i, j-1, idx+1):
                        return True
                if j < len(board[0])-1 and ((i, j+1) not in seen):
                    if search(i, j+1, idx+1):
                        return True

                seen.remove((i, j))
            return False

            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if search(i, j, 0):
                    return True

                seen = set()


        return False