class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def solve(par_string: list, num_open: int, num_closed: int):
            if len(par_string) == n*2 and num_open == num_closed:
                res.append(''.join(par_string))
                return

            if num_open < n:
                # Option 1: Add opening parenthesis
                par_string.append('(')
                solve(par_string, num_open + 1, num_closed)
                par_string.pop()

            if num_open > num_closed:
                # Option 2: Add closing parenthesis
                par_string.append(')')
                solve(par_string, num_open, num_closed + 1)
                par_string.pop()

        solve([], 0, 0)
        return res