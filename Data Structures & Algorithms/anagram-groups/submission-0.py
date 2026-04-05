class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = {}
        for string in strs:
            char_list = [char for char in string]
            char_list.sort()
            sorted_str = ''
            for char in char_list:
                sorted_str += char
            if sorted_str in sorted_strs:
                sorted_strs[sorted_str].append(string)
            else:
                sorted_strs[sorted_str] = [string]
        return [component for component in sorted_strs.values()]
