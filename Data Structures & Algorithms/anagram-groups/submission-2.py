class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for string in strs:
            key = "".join(sorted(string))
            if key not in group:
                group[key] = []
            group[key].append(string)
        result = []
        for value in group.values():
            result.append(value)
        return result