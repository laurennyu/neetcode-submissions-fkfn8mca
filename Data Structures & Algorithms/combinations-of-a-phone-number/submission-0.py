class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        if len(digits) == 0:
            return res

        num_to_letters = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

        def solve(candidate: list, idx: int):
            nonlocal res, num_to_letters

            if idx >= len(digits):
                res.append(''.join(candidate))
                return

            for letter in num_to_letters[int(digits[idx])]:
                candidate.append(letter)
                solve(candidate, idx + 1)
                candidate.pop()

        solve([], 0)
        return res