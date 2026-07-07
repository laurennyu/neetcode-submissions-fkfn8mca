class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = set()
        def comb_sum(idx, target, comb):
            # Find all combinations that sum to target
            nonlocal candidates, res

            # Base case: invalid idx
            if idx >= len(candidates):
                return
            
            if candidates[idx] == target:
                # Reached target
                res.add(tuple(sorted(comb.copy() + [candidates[idx]])))

            if candidates[idx] < target:
                # Take this number
                comb_sum(idx+1, target-candidates[idx], comb.copy() + [candidates[idx]])

            # Don't take this number: Need to skip to next non-duplicate
            curr_num = candidates[idx]
            idx += 1
            while idx < len(candidates) and candidates[idx] == curr_num:
                idx += 1

            comb_sum(idx, target, comb)

        comb_sum(0, target, [])
        return [list(comb) for comb in res]