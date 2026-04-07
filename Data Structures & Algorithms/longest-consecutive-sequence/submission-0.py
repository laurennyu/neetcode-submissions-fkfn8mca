class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = {}
        components = [] # list of component [start, end] indices, inclusive
        for num in nums:
            if num not in seen:
                if num - 1 in seen:
                    # add to prev's component
                    comp_idx = seen[num - 1]
                    components[comp_idx][1] = num
                    seen[num] = comp_idx
                elif num + 1 in seen:
                    # add to next's component
                    comp_idx = seen[num + 1]
                    components[comp_idx][0] = num
                    seen[num] = comp_idx
                else:
                    # add new component
                    seen[num] = len(components)
                    components.append([num, num])

        if len(components) == 0:
            return 0
        if len(components) == 1:
            return components[0][1] - components[0][0] + 1
        
        # coalesce
        max_length = 0
        component_idxs = list(range(len(components)))
        while len(component_idxs) > 0:
            comp_idx = component_idxs.pop()
            comp_start = components[comp_idx][0]
            comp_end = components[comp_idx][1]
            while comp_start - 1 in seen:
                # coalesce
                other_comp_idx = seen[comp_start - 1]
                if other_comp_idx in component_idxs:
                    component_idxs.remove(other_comp_idx)
                    comp_start = components[other_comp_idx][0]
            while comp_end + 1 in seen:
                # coalesce
                other_comp_idx = seen[comp_end + 1]
                if other_comp_idx in component_idxs:
                    component_idxs.remove(other_comp_idx)
                    comp_end = components[other_comp_idx][1]
            max_length = max(max_length, comp_end - comp_start + 1)

        return max_length