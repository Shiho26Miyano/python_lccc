class Solution:
    #hashmap o(n) o(n) 
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        count = {}
        pos = -1
        for index, letter in enumerate(s):
            if letter in count and count[letter] > pos:
                pos = count[letter]
            count[letter] = index 
            output = max(output,index-pos)
        return output
    

    
    # deque o(n) o(n) 
    def lengthOfLongestSubstring2(self, s: str) -> int:
        res = 0
        q = deque()
        for c in s:
            if c in q:
                while q.popleft() != c:
                    pass
            q.append(c)
            res = max(res, len(q))
        
        return res


