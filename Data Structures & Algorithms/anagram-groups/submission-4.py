from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupDict = defaultdict(list)
        for st in strs:
            count = [0] * 26
            for char in st:
                count[ord(char) - ord('a')] += 1
            groupDict[tuple(count)].append(st)

        return [item for item in groupDict.values()]