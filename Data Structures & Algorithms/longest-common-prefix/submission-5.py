class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs:
            return ""

        lcp=""
        prefix = strs[0][0]
        n = len(strs[0])
        for i in range(len(strs[0])):
            for st in strs:
                if not st.startswith(prefix):
                    return lcp
            lcp = prefix
            if i + 1 < n:
                prefix = prefix + strs[0][i+1]
        return prefix