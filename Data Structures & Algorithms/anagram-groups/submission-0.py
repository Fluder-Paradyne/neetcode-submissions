class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouping = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in grouping:
                grouping[key] = []
            grouping[key].append(word)
        
        return [group for group in grouping.values()]