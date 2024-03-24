class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = defaultdict(int)
        for w in s:
            map[w] +=1 
        for w in t:
            map[w] -= 1
        for val in map.values():
            if val != 0:
                return False
        return True
        