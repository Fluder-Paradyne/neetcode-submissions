from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupDict = defaultdict(list)
        for st in strs:
            groupDict["".join(sorted(st))].append(st)
        
        return [item for item in groupDict.values()]