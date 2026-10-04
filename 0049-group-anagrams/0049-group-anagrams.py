class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        groups = {}
        
        for x in strs:
            key = ''.join(sorted(x))

            if key not in groups:
                groups[key] = []

            groups[key].append(x)

        return list(groups.values())
