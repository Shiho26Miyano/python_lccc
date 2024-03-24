class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ##defaultdict provides default value for non existing key with the value returned by the factory fucntion int->0 
        map = defaultdict(int)
        for w in s:
            map[w] +=1 
        for w in t:
            map[w] -= 1
        for val in map.values():
            if val != 0:
                return False
        return True
        