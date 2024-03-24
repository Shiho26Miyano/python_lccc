class Solution:
    def containsDuplicateMap(self, nums: List[int]) -> bool:
        map = {}
        for n in nums:
            if n in map:
                return True
            map[n] = n
        return False
    
    def containsDuplicateSet(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
