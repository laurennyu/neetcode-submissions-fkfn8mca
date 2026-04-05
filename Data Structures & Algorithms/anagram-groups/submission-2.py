class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map of string (sorted) to list of strings that match
        sorted_strs = {}
        # For each string, sort the characters
        for string in strs:
            sorted_chars = sorted(string)
            sorted_str = ''.join(sorted_chars)
            # for char in sorted_chars:
            #     sorted_str += char
            if sorted_str in sorted_strs:
                sorted_strs[sorted_str].append(string)
            else:
                sorted_strs[sorted_str] = [string]
        return [component for component in sorted_strs.values()]
