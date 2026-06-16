class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Let paths[i][j] be the number of paths that can get to point i,j
        # only going down or right
        paths = [[1] * n] # Base case: only one way to travel first row (right)
        for i in range(1, m):
            row = [paths[i-1][0]] # Base case: only one way to get to first tile in row (down)
            for j in range(1, n):
                row.append(row[-1] + paths[i-1][j])

            paths.append(row)

        return paths[-1][-1]