class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for w in strs:
            sorted_word = ''.join(sorted(w))
            map[sorted_word].append(w)
        return list(map.values())